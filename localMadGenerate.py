from statistics import median
import csv

import numpy
import pandas as pd


# function to find MAD
def mad(numbers, M):
    ad = list()
    for i in numbers:
        ad.append(abs(i - M))

    return median(ad)


# variables for contains local profile data
# <-------------------------------->
tableX = list()
tableY = list()
tableIntensity = list()

# fill list in to table equal to number of index( can be more than but cannot be less than number of index)
for i in range(1, 290):
    tableX.append([])
    tableY.append([])
    tableIntensity.append([])
# <-------------------------------->

# variable for mark the first position of localProfile
pointer = 1

# variable for choose range of local profiles
localRange = 100

# variable for track last profile
lastPosition = 12883

# loop for all profiles
for i in range(1, lastPosition + 1):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')

    # store current profile X, Y, Intensity in local variables set
    for row in df.iterrows():
        tableX[row[0]].append(row[1].X)
        tableY[row[0]].append(row[1].Y)
        tableIntensity[row[0]].append(row[1].Intensity)

    # check if already store all local range profiles or already reach last profile
    if i % localRange == 0 or i == lastPosition:
        # variables to keep median of all point
        medianProfileX = list()
        medianProfileY = list()
        medianProfileIntensity = list()

        # find median profile of localRange and keep in variables
        for j in range(len(tableX)):
            try:
                medianProfileX.append(median(tableX[j - 1]))
                medianProfileY.append(median(tableY[j - 1]))
                medianProfileIntensity.append(median(tableIntensity[j - 1]))
            except:
                medianProfileX.append(0)
                medianProfileY.append(0)
                medianProfileIntensity.append(0)

        # write median profile to CSV
        with open('localMedian/medianProfile' + str(pointer) + "-" + str(i) + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['X', 'Y', 'Intensity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for a, b, c in zip(medianProfileX, medianProfileY, medianProfileIntensity):
                writer.writerow({'X': '' + str(a), 'Y': '' + str(b), 'Intensity': '' + str(c)})

        # variables to keep MAD of all point
        madY = list()
        madTop = list()
        madBottom = list()

        # find every MAD of local profiles
        for m in range(len(tableY)):
            M = medianProfileY[m - 1]
            try:
                Mad = mad(tableY[m], M)
            except:
                Mad = 0

            # store MAD and roof and floor of MAD in variables
            madY.append(Mad)
            madTop.append(M + 3 * Mad)
            madBottom.append(M - 3 * Mad)

        # write all MAD in CSV
        with open('localMAD/mad' + str(pointer) + "-" + str(i) + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['MAD', 'MAD_Top', 'MAD_Bottom']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for a, b, c in zip(madY, madTop, madBottom):
                writer.writerow({'MAD': '' + str(a), 'MAD_Top': '' + str(b), 'MAD_Bottom': '' + str(c)})

        # change first position of local profiles
        pointer = i

        # reset variables for contains local profile data
        # <-------------------------------->
        tableX = list()
        tableY = list()
        tableIntensity = list()

        for z in range(1, 290):
            tableX.append([])
            tableY.append([])
            tableIntensity.append([])
        # <-------------------------------->