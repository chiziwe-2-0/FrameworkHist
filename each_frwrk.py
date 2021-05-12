import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

index = np.arange(8)
headers = ['metric', 'value']
df1 = pd.read_csv('C:/Users/nikit/Desktop/Bench_Frameworks/data/each_frwrk/falcon512.csv', names=headers)
df2 = pd.read_csv('C:/Users/nikit/Desktop/Bench_Frameworks/data/each_frwrk/falconpypy512.csv', names=headers)

x1 = df1['metric'][1::]
y1 = df1['value'][1::]

x2 = df2['metric'][1::]
y2 = df2['value'][1::]



# plot

name = 'Falcon 3.0.1 (512)'
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
