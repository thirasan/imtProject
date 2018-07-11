from statistics import median
import csv

import numpy
import pandas as pd


def mad(numbers, M):

    ad = list()
    for i in numbers:
        ad.append(abs(i-M))

    return median(ad)


tableX = numpy.zeros(shape=(202, 12884))
tableY = numpy.zeros(shape=(202, 12884))
tableIntensity = numpy.zeros(shape=(202, 12884))

for i in range(1, 12884):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    for row in df.iterrows():
        tableX[row[0]][i-1] = row[1].X
        tableY[row[0]][i-1] = row[1].Y
        tableIntensity[row[0]][i-1] = row[1].Intensity

madY = list()
madTop = list()
madBottom = list()

for i in range(len(tableY)):
    M = median(tableY[i])
    Mad = mad(tableY[i], M)
    madY.append(Mad)
    madTop.append(M + 10*Mad)
    madBottom.append(M - 10*Mad)

with open('MAD.csv', 'w', newline='') as csvfile:
    fieldnames = ['MAD', 'MAD_Top', 'MAD_Bottom']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, j, k in zip(madY, madTop, madBottom):
        writer.writerow({'MAD': '' + str(i), 'MAD_Top': '' + str(j), 'MAD_Bottom': '' + str(k)})
