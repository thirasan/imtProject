import matplotlib.pyplot as plt
import pandas as pd
import csv

df_median_profile = pd.read_csv('medianProfile.csv')
df_mad = pd.read_csv('MAD.csv')

# for i in range(1, 12884):
#
#     x = list()
#     y = list()
#     intensity = list()
#
#     df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
#     for row, rangeMad, medianPro in zip(df.iterrows(), df_mad.iterrows(), df_median_profile.iterrows()):
#         x.append(row[1].X)
#         intensity.append(row[1].Intensity)
#         if rangeMad[1].MAD_Top < row[1].Y < rangeMad[1].MAD_Bottom:
#             y.append(row[1].Y)
#         else:
#             y.append(medianPro[1].Y)
#     with open('profile_no1_data/profile' + str(i) + '.csv', 'w', newline='') as csvfile:
#         fieldnames = ['X', 'Y', 'Intensity']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#         writer.writeheader()
#         for a, j, k in zip(x, y, intensity):
#             writer.writerow({'X': '' + str(a), 'Y': '' + str(j), 'Intensity': '' + str(k)})

plt.figure(1)
plt.suptitle('medianRange', fontsize=14, fontweight='bold')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.plot(df_median_profile.X, df_median_profile.Y, 'ro', markersize=1, color='red')
plt.plot(df_median_profile.X, df_median_profile.Intensity, 'ro', markersize=1, color='blue')
plt.plot(df_median_profile.X, df_mad.MAD_Top, 'ro', markersize=1, color='greenyellow')
plt.plot(df_median_profile.X, df_mad.MAD_Bottom, 'ro', markersize=1, color='greenyellow')

plt.show()