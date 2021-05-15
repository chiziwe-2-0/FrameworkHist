import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

index = np.arange(5)
x = ["Django", "Flask", "Bottle", "CherryPy", "Falcon"]

cpython64_get = [2166.0, 4758.0, 4826.0, 591.0, 6181.0]
pypy64_get = [3020.0, 4975.0, 6480.0, 1844.0, 6236.0]

cpython64_post = [1300.0, 3394.0, 3624.0, 1440.0, 3747.0]
pypy64_post = [2238.0, 4409.0, 4227.0, 1323.0, 4715.0]

cpython512_get = [1749.0, 4191.0, 4461.0, 1554.0, 5605.0]
pypy512_get = [3023.0, 4314.0, 5189.0, 1774.0, 5655.0]

cpython512_post = [1369.0, 3649.0, 3621.0, 1412.0, 5032.0]
pypy512_post = [2010.0, 3653.0, 4225.0, 1343.0, 5214.0]

data = {'CPython 3.9': cpython512_get,
        'PyPy 7.3.4': pypy512_get}

df = pd.DataFrame(data)
df.plot(kind='bar')

name = 'GET-запросы (512 подключений)'

plt.title(name)
plt.xticks(index, x, rotation=20)

plt.ylabel("Количество запросов в секунду")
plt.savefig(name + ".svg")

plt.grid(linestyle='--', linewidth=0.5)
plt.show()







