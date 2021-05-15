import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
from sshtunnel import SSHTunnelForwarder

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

# Create a database connection
conn = psycopg2.connect(
    database='benchmark',
    user='postgres',
    host=tunnel.local_bind_host,
    port=tunnel.local_bind_port,
)

rest = 'limit 8 offset 16'
get = 'limit 8'

# Задать параметры
request = rest
framework_name = "'falcon'"
level = 64


framework_nameWithoutLast = framework_name[:-1]
framework_nameWithoutAll = framework_name[1:-1]
framework_namePyPy = framework_nameWithoutLast + "pypy'"
level = str(level)

if request == 'limit 8':
    name = framework_nameWithoutAll[0].upper()+framework_nameWithoutAll[1:] + " (" + level + ", GET-запросы)"
else:
    name = framework_nameWithoutAll[0].upper()+framework_nameWithoutAll[1:] + " (" + level + ", REST-запросы)"


sql = """select metric, value from "result" where framework = """ + framework_name + """ and "level" = """ + level + """ and (metric = 'minimum_latency' or metric = 'maximum_latency' or metric = 'average_latency' or metric = 'percentile_50' or metric = 'percentile_75' or metric = 'percentile_90' or metric = 'percentile_99' or metric = 'percentile_99.999') """ + request + """;"""
sqlPyPy = """select metric, value from "result" where framework = """ + framework_namePyPy + """ and "level" = """ + level + """ and (metric = 'minimum_latency' or metric = 'maximum_latency' or metric = 'average_latency' or metric = 'percentile_50' or metric = 'percentile_75' or metric = 'percentile_90' or metric = 'percentile_99' or metric = 'percentile_99.999') """ + request + """;"""

dat = sqlio.read_sql_query(sql, conn)
datPyPy = sqlio.read_sql_query(sqlPyPy, conn)
conn = None

# Stop the tunnel
tunnel.stop()

print(dat)
print(datPyPy)

index = np.arange(8)

x1 = dat['metric']
y1 = dat['value']

x2 = datPyPy['metric']
y2 = datPyPy['value']

plt.title(name)
plt.xlabel("Показатель")
plt.ylabel("Время ожидания, мс")

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(["CPython 3.9", "PyPy 7.3.4"])

plt.grid(True)

plt.xticks(index, x1, rotation=30)

plt.tight_layout()
plt.fill_between(x1, y1, alpha=0.30)
plt.fill_between(x2, y2, alpha=0.30)

plt.savefig(name + ".svg")
plt.show()
