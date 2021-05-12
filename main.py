import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x64 = ["django", "flask", "bottle", "cherrypy", "falcon"]
cpython64 = [2166.0, 3394.0, 4021.0, 591.0, 4774.0]
pypy64 = [3020.0, 6236.0, 6480.0, 1844.0, 6236.0]

headers = ['metric', 'value']
df = pd.read_csv('C:/Users/nikit/Desktop/Bench_Frameworks/data/django64.csv', names=headers)
print(df)

x = df['metric']
y = df['value']

print(x)

# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()


x = np.arange(1, 8)

data_1 = np.random.randint(2, 15, size=7)
data_2 = np.random.randint(3, 20, size=7)

fig, ax = plt.subplots()

ax.bar(x, data_1)
ax.bar(x, data_2, bottom=data_1)

fig.set_figwidth(12)  # ширина и
fig.set_figheight(6)  # высота "Figure"

fig.set_facecolor('floralwhite')
ax.set_facecolor('seashell')

plt.fill_between(x,y)
plt.show()
