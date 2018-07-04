from scipy.stats import norm

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('allProfilePlot.csv')

p1 = df.P1.values
p2 = df.P2.values
p3 = df.P3.values
p4 = df.P4.values

colors = ['red', 'tan', 'lime', 'blue']
n, bins, patches = plt.hist([p1, p2, p3, p4], color=colors, alpha=0.5)
plt.show()
