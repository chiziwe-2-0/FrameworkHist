import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

index = np.arange(5)
x = ["Django", "Flask", "Bottle", "CherryPy", "Falcon"]

cpython64 = [2166.0, 3394.0, 4021.0, 591.0, 4774.0]
pypy64 = [3020.0, 4409.0, 6480.0, 1844.0, 6236.0]

cpython512 = [1749.0, 4191.0, 4461.0, 1554.0, 5214.0]
pypy512 = [3023.0, 4314.0, 5189.0, 1774.0, 5605.0]

data = {'CPython': cpython64,
        'PyPy': pypy64}

df = pd.DataFrame(data)
df.plot(kind='bar')

name = 'Количество запросов в секунду (64)'
plt.title(name)
plt.xticks(index, x, rotation=20)

plt.savefig(name + ".svg")

plt.show()







