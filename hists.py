import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

index = np.arange(2)
x = ["Django 4.04", "Flask 2.1.1"]

# 2.7.2
cpython64_get_272 = [8400.0, 8743.0]
pypy64_get_272 = [9369.0, 7540.0]
jython64_get_272 = [7820.0, 10802.0]

cpython64_post_272 = [7021.0, 6917.0]
pypy64_post_272 = [7200.0, 6802.0]
jython64_post_272 = [1090.0, 1297.0]

cpython512_get_272 = [7885.0, 8197.0]
pypy512_get_272 = [8549.0, 7154.0]
jython512_get_272 = [7126.0, 7467.0]

cpython512_post_272 = [6318.0, 6317.0]
pypy512_post_272 = [6524.0, 6398.0]
jython512_post_272 = [3443.0, 4558.0]

# 3.9
cpython64_get = [3510.0, 8658.0]
pypy64_get = [9133.0, 7601.0]

cpython64_post = [2861.0, 6917.0]
pypy64_post = [6753.0, 6243.0]

cpython512_get = [3591.0, 7645.0]
pypy512_get = [8569.0, 7293.0]

cpython512_post = [3201.0, 5799.0]
pypy512_post = [6524.0, 6026.0]


data = {'CPython 3.9': cpython64_post,
        'PyPy 3.9': pypy64_post}

'''
data = {'CPython 2.7.2': cpython512_post_272,
        'PyPy 2.7': pypy512_post_272,
        'Jython 2.7.2': jython512_post_272}
'''

df = pd.DataFrame(data)
df.plot(kind='bar')

name = 'POST-запросы (64 подключений) (Python 3.9)'

plt.title(name)
plt.xticks(index, x, rotation=0)

plt.ylabel("Количество запросов в секунду")
plt.savefig(name + ".svg")

plt.grid(linestyle='--', linewidth=0.5)
plt.show()







