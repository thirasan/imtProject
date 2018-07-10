from statistics import median
import matplotlib.pyplot as plt

import numpy
import pandas as pd


# def mean(numbers):
#     return float(sum(numbers)) / max(len(numbers), 1)


pa1 = list()
pa2 = list()
pa3 = list()
pa4 = list()

tableX = numpy.zeros(shape=(202, 345))
tableY = numpy.zeros(shape=(202, 345))
tableIntensity = numpy.zeros(shape=(202, 345))

for i in range(1, 345):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    for row in df.iterrows():
        tableX[row[0]][i] = row[1].X
        tableY[row[0]][i] = row[1].Y
        tableIntensity[row[0]][i] = row[1].Intensity

medianProfileX = list()
medianProfileY = list()
medianProfileIntensity = list()

for i in range(len(tableX)):
    medianProfileX.append(median(tableX[i]))
    medianProfileY.append(median(tableY[i]))
    medianProfileIntensity.append(median(tableIntensity[i]))

plt.figure(i)
plt.suptitle('Profile' + str(i), fontsize=14, fontweight='bold')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# plot every point
plt.plot(medianProfileX, medianProfileY, 'ro', markersize=1, color='red')
plt.plot(medianProfileX, medianProfileIntensity, 'ro', markersize=1, color='blue')
plt.show()

