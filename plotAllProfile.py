from statistics import median

import matplotlib.pyplot as plt
import pandas as pd


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


df = pd.read_csv('allProfilePlot.csv')

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