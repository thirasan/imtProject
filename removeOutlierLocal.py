import matplotlib.pyplot as plt
import pandas as pd
import csv


df_median_profile = pd.read_csv('localMedian/medianProfile1-100.csv')

plt.figure(1)
plt.suptitle('medianRange', fontsize=14, fontweight='bold')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(df_median_profile.X, df_median_profile.Y, 'ro', markersize=1, color='red')
plt.plot(df_median_profile.X, df_median_profile.Intensity, 'ro', markersize=1, color='blue')

plt.show()