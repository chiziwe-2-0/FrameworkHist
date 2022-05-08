import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
from sshtunnel import SSHTunnelForwarder

'''
# Create an SSH tunnel
tunnel = SSHTunnelForwarder(
    ('localhost', 2222),
    ssh_username='vagrant',
    ssh_private_key='C:/Users/nikit/Desktop/private_key',
    remote_bind_address=('localhost', 5432),
    local_bind_address=('localhost', 6543)
)
# Start the tunnel
tunnel.start()
'''

# Create a database connection
conn = psycopg2.connect(
    database='benchmark',
    user='postgres',
    host='localhost',
    port=5432,
)

post = 'limit 8 offset 16'
get = 'limit 8'

# Задать параметры
request = get
framework_name = "'flask'"
level = 64


framework_nameWithoutLast = framework_name[:-1]
framework_nameWithoutAll = framework_name[1:-1]
framework_namePyPy = framework_nameWithoutLast + "_pypy'"
#framework_nameJython = framework_nameWithoutLast + "_jython'"


level = str(level)

if request == 'limit 8':
    name = framework_nameWithoutAll[0].upper()+framework_nameWithoutAll[1:] + " (" + level + " подключений, GET-запросы)"
else:
    name = framework_nameWithoutAll[0].upper()+framework_nameWithoutAll[1:] + " (" + level + " подключений, POST-запросы)"


sql = """select metric, value from "result" where framework = """ + framework_name + """ and "level" = """ + level + """ and (metric = 'Минимальная задержка' or metric = 'Максимальная задержка' or metric = 'Средняя задержка' or metric = 'Перцентиль 50' or metric = 'Перцентиль 75' or metric = 'Перцентиль 90' or metric = 'Перцентиль 99' or metric = 'Перцентиль 99.999') """ + request + """;"""
sqlPyPy = """select metric, value from "result" where framework = """ + framework_namePyPy + """ and "level" = """ + level + """ and (metric = 'Минимальная задержка' or metric = 'Максимальная задержка' or metric = 'Средняя задержка' or metric = 'Перцентиль 50' or metric = 'Перцентиль 75' or metric = 'Перцентиль 90' or metric = 'Перцентиль 99' or metric = 'Перцентиль 99.999') """ + request + """;"""
# sqlJython = """select metric, value from "result" where framework = """ + framework_nameJython + """ and "level" = """ + level + """ and (metric = 'Минимальная задержка' or metric = 'Максимальная задержка' or metric = 'Средняя задержка' or metric = 'Перцентиль 50' or metric = 'Перцентиль 75' or metric = 'Перцентиль 90' or metric = 'Перцентиль 99' or metric = 'Перцентиль 99.999') """ + request + """;"""


dat = sqlio.read_sql_query(sql, conn)
datPyPy = sqlio.read_sql_query(sqlPyPy, conn)
#dataJython = sqlio.read_sql_query(sqlJython, conn)
conn = None

# Stop the tunnel
# tunnel.stop()

print(dat)
print(datPyPy)
#print(dataJython)

index = np.arange(8)
print(index)

x1 = dat['metric']
y1 = dat['value']

x2 = datPyPy['metric']
y2 = datPyPy['value']

#x3 = dataJython['metric']
#y3 = dataJython['value']

plt.title(name)
plt.xlabel("Показатель")
plt.ylabel("Время ожидания, мс")

plt.plot(x1, y1)
plt.plot(x2, y2)
# plt.plot(x3, y3)

plt.legend(["CPython 3.9", "PyPy 3.9"])
#plt.legend(["CPython 2.7.2", "PyPy 2.7", "Jython 2.7.2"])

plt.grid(True)

plt.xticks(index, x1, rotation=30)

plt.tight_layout()
plt.fill_between(x1, y1, alpha=0.30)
plt.fill_between(x2, y2, alpha=0.30)
#plt.fill_between(x3, y3, alpha=0.30)

plt.savefig(name + ".svg")
plt.show()
