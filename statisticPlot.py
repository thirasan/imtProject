from scipy.stats import norm

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('profile_no1_data/profile1.csv')

fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = norm.stats(moments='mvsk')

x = df.Y.values
ax.plot(x, norm.pdf(x),
       'r-', lw=5, alpha=0.6, label='norm pdf')

rv = norm()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

r = norm.rvs(size=300)

ax.hist(x, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()