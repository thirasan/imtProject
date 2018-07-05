import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('allProfilePlot.csv')

plt.figure(1)
plt.suptitle('Profile', fontsize=14, fontweight='bold')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(df.P1, df.index, 'ro', markersize=1, color='red')
plt.plot(df.P2, df.index, 'ro', markersize=1, color='orange')
plt.plot(df.P3, df.index, 'ro', markersize=1, color='green')
plt.plot(df.P4, df.index, 'ro', markersize=1, color='brown')

plt.axis([-10, 20, -10, 310])

plt.show()