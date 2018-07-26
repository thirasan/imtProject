from statistics import median

import matplotlib.pyplot as plt
import pandas as pd


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def average(lst):
    return sum(lst) / len(lst)


df = pd.read_csv('allProfilePlot.csv')

thickness1 = list()
thickness2 = list()

for row in df.iterrows():
    thickness1.append(row[1].PY2 - row[1].PY1)
    thickness2.append(row[1].PY4 - row[1].PY3)

print(str(mean(thickness1)) + "  " + str(average(thickness1)))
print(str(mean(thickness2)) + "  " + str(average(thickness2)))

plt.figure(1)
plt.suptitle('Profile', fontsize=14, fontweight='bold')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(df.PX1, df.index, 'ro', markersize=1, color='red')
plt.plot(df.PX2, df.index, 'ro', markersize=1, color='orange')
plt.plot(df.PX3, df.index, 'ro', markersize=1, color='green')
plt.plot(df.PX4, df.index, 'ro', markersize=1, color='brown')



# plt.axis([-15, 20, -100, 12984])

plt.show()