from statistics import median
import csv

import numpy
import pandas as pd


def mad(numbers, M):

    ad = list()
    for i in numbers:
        ad.append(abs(i-M))

    return median(ad)


tableX = list()
tableY = list()
tableIntensity = list()

for i in range(1, 290):
    tableX.append([])
    tableY.append([])
    tableIntensity.append([])

pointer = 1

for i in range(1, 1705):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    for row in df.iterrows():
        tableX[row[0]].append(row[1].X)
        tableY[row[0]].append(row[1].Y)
        tableIntensity[row[0]].append(row[1].Intensity)

    if i % 100 == 0 or i == 1705:
        medianProfileX = list()
        medianProfileY = list()
        medianProfileIntensity = list()

        for j in range(len(tableX)):
            try:
                medianProfileX.append(median(tableX[j - 1]))
                medianProfileY.append(median(tableY[j - 1]))
                medianProfileIntensity.append(median(tableIntensity[j - 1]))
            except:
                medianProfileX.append(0)
                medianProfileY.append(0)
                medianProfileIntensity.append(0)

        with open('localMedian/medianProfile' + str(pointer) + "-" + str(i) + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['X', 'Y', 'Intensity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for a, b, c in zip(medianProfileX, medianProfileY, medianProfileIntensity):
                writer.writerow({'X': '' + str(a), 'Y': '' + str(b), 'Intensity': '' + str(c)})

        madY = list()
        madTop = list()
        madBottom = list()

        for m in range(len(tableY)):
            M = medianProfileY[m-1]
            try:
                Mad = mad(tableY[m], M)
            except:
                Mad = 0
            madY.append(Mad)
            madTop.append(M + 3 * Mad)
            madBottom.append(M - 3 * Mad)

        with open('localMAD/mad' + str(pointer) + "-" + str(i) + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['MAD', 'MAD_Top', 'MAD_Bottom']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for a, b, c in zip(madY, madTop, madBottom):
                writer.writerow({'MAD': '' + str(a), 'MAD_Top': '' + str(b), 'MAD_Bottom': '' + str(c)})

        pointer = i

        tableX = list()
        tableY = list()
        tableIntensity = list()

        for z in range(1, 290):
            tableX.append([])
            tableY.append([])
            tableIntensity.append([])