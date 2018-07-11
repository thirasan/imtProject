from statistics import median
import csv

import numpy
import pandas as pd


tableX = numpy.zeros(shape=(202, 345))
tableY = numpy.zeros(shape=(202, 345))
tableIntensity = numpy.zeros(shape=(202, 345))

for i in range(1, 345):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    for row in df.iterrows():
        tableX[row[0]][i-1] = row[1].X
        tableY[row[0]][i-1] = row[1].Y
        tableIntensity[row[0]][i-1] = row[1].Intensity

medianProfileX = list()
medianProfileY = list()
medianProfileIntensity = list()

for j in range(len(tableX)):
    medianProfileX.append(median(tableX[j-1]))
    medianProfileY.append(median(tableY[j-1]))
    medianProfileIntensity.append(median(tableIntensity[j-1]))

with open('medianProfile.csv', 'w', newline='') as csvfile:
    fieldnames = ['X', 'Y', 'Intensity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for a, b, c in zip(medianProfileX, medianProfileY, medianProfileIntensity):
        writer.writerow({'X': '' + str(a), 'Y': '' + str(b), 'Intensity': '' + str(c)})
