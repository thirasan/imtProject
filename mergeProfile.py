from json.decoder import NaN

import matplotlib.pyplot as plt
import pandas as pd
import csv


# function which return means value
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


# function which return average
def average(lst):
    return sum(lst) / len(lst)


# function to find p2 point
def p2Detect(df):
    # First while loop will continue from the first 254 intensity point and continue check to
    # the last 254 intensity point until it find first ceramic point which have 254 intensity

    # pointer is for move the current 254 intensity index
    pointer = 0

    while True:
        # check if Y-axis of the current point is nearly to mean of all 254 intensity point
        # then it should be ceramic point
        if saturation.iloc[0 + pointer].Y > mean(list(saturation.Y)) - 0.2:

            # keep first ceramic point to index_of_p2
            index_of_p2 = saturation.index[0 + pointer]

            # localMean is mean of the 5 index Y-axis after the first ceramic point
            localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 + 1].Y, df.loc[index_of_p2 + 2].Y, df.loc[index_of_p2 + 3].Y,
                              df.loc[index_of_p2 + 4].Y])

            # loop from current index to index 0 and stop when Y-axis of current index is outlier
            while localMean + 1.5 > df.loc[index_of_p2].Y > localMean - 1.5:

                # end the loop when index_of_p2 is nearly begining index
                if index_of_p2 < 10:
                    # index_of_p2 = saturation.index[0 + pointer]
                    break

                index_of_p2 -= 1

            # return index of p2 and p2 point which contains x and y value
            return index_of_p2, df.loc[index_of_p2]
        # if not most current point forward
        else:
            pointer += 1
            continue


# function to find p3 point
def p3Detect(df):
    # First while loop will continue from the last 254 intensity point and continue check back to the first
    # 254 intensity point until it find last ceramic point which have 254 intensity

    # pointer is for move the current 254 intensity index
    pointer = 0

    while True:
        # check if the current point is nearly to mean of all 254 intensity point then it should be ceramic point
        if saturation.iloc[-(1 + pointer)].Y > mean(list(saturation.Y)) - 0.2:

            # keep last ceramic point to index_of_p3
            index_of_p3 = saturation.index[-(1 + pointer)]

            # localMean is mean of the 5 index Y-axis before the last ceramic point
            localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 - 1].Y, df.loc[index_of_p3 - 2].Y, df.loc[index_of_p3 - 3].Y,
                              df.loc[index_of_p3 - 4].Y])

            # loop from current index to the last index and stop when Y-axis of current index is outlier
            while localMean + 1.5 > df.loc[index_of_p3].Y > localMean - 1.5:
                if index_of_p3 > len(df.index) - 10:
                    index_of_p3 -= 1
                    # index_of_p3 = saturation.index[-(1 + pointer)]
                    break
                index_of_p3 += 1
            return index_of_p3, df.loc[index_of_p3]
        # if not move current point backward
        else:
            pointer += 1
            continue


# function to find the p1 point according to p2 index
def p1Detect(df, index_of_p2):
    # start from p2 index
    currentPoint = index_of_p2

    # loop from p2 index to index 0
    while True:
        # localAverage is mean of the 8 index Y-axis before the current point
        localAverage = average([df.loc[currentPoint].Y, df.loc[currentPoint - 1].Y, df.loc[currentPoint - 2].Y,
                          df.loc[currentPoint - 3].Y, df.loc[currentPoint - 4].Y, df.loc[currentPoint - 5].Y,
                          df.loc[currentPoint - 6].Y, df.loc[currentPoint - 7].Y, df.loc[currentPoint - 8].Y])

        # check if current point is nearly to localAverage
        if localAverage + 0.5 > df.loc[currentPoint].Y > localAverage - 0.5:

            # check for sure that point we take is not just a mistake point
            # if next 5 point is also nearly averagePoint then it must be correct point
            # <--------------------------------->
            for k in range(1, 6):
                temp = average([df.loc[currentPoint + k].Y, df.loc[currentPoint - 1 + k].Y,
                             df.loc[currentPoint - 2 + k].Y, df.loc[currentPoint - 3 + k].Y,
                             df.loc[currentPoint - 4 + k].Y, df.loc[currentPoint - 5 + k].Y])
                if temp + 0.5 > df.loc[currentPoint + k].Y > temp - 0.5:
                    check = True
                    continue
                else:
                    check = False
                    break

            if check is False:
                currentPoint -= 1
                continue
            # <--------------------------------->

            # return currentPoint as p1 index and p1 x and y value
            return currentPoint, df.loc[currentPoint]
        # if not move current point backward
        else:
            currentPoint -= 1
            continue


# function to find the p4 point according to p3 index
def p4Detect(df, index_of_p3):
    # start from p3 index
    currentPoint = index_of_p3

    # loop from p3 index to last index
    while True:
        # localAverage is mean of the 8 index Y-axis after the current point
        localAverage = average([df.loc[currentPoint].Y, df.loc[currentPoint + 1].Y, df.loc[currentPoint + 2].Y,
                                df.loc[currentPoint + 3].Y, df.loc[currentPoint + 4].Y, df.loc[currentPoint + 5].Y,
                                df.loc[currentPoint + 6].Y, df.loc[currentPoint + 7].Y, df.loc[currentPoint + 8].Y])

        # check if current point is nearly to localAverage
        if localAverage + 0.5 > df.loc[currentPoint].Y > localAverage - 0.5:

            # check for sure that point we take is not just a mistake point
            # if next 5 point is also nearly averagePoint then it must be correct point
            # <--------------------------------->
            for k in range(1, 6):
                temp = average([df.loc[currentPoint + k].Y, df.loc[currentPoint + 1 + k].Y, df.loc[currentPoint + 2 + k].Y,
                                df.loc[currentPoint + 3 + k].Y, df.loc[currentPoint + 4 + k].Y, df.loc[currentPoint + 5 + k].Y])
                if temp + 0.5 > df.loc[currentPoint + k].Y > temp - 0.5:
                    check = True
                    continue
                else:
                    check = False
                    break

            if check is False:
                currentPoint += 1
                continue
            # <--------------------------------->

            # return currentPoint as p4 index and p4 x and y value
            return currentPoint, df.loc[currentPoint]
        # if not move current point forward
        else:
            currentPoint += 1
            continue


# variables to keep all p1, p2, p3, and p4
px1 = list()
px2 = list()
px3 = list()
px4 = list()

py1 = list()
py2 = list()
py3 = list()
py4 = list()

# loop for every profiles
for i in range(1, 12884):
    try:
        df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
        # saturation variable contain only 254 value
        saturation = df.loc[df['Intensity'] > 253]

        # call function to find significant point
        index_of_p2, p2 = p2Detect(df)
        index_of_p3, p3 = p3Detect(df)
        index_of_p1, p1 = p1Detect(df, index_of_p2)
        index_of_p4, p4 = p4Detect(df, index_of_p3)

        # add X-axis of p1-p4 to variable
        px1.append(p1.X)
        px2.append(p2.X)
        px3.append(p3.X)
        px4.append(p4.X)

        # add Y-axis of p1-p4 to variable
        py1.append(p1.Y)
        py2.append(p2.Y)
        py3.append(p3.Y)
        py4.append(p4.Y)
    except:
        # if cannot find significant point then add NaN instead
        print("Error with file" + str(i))
        px1.append(NaN)
        px2.append(NaN)
        px3.append(NaN)
        px4.append(NaN)

        py1.append(NaN)
        py2.append(NaN)
        py3.append(NaN)
        py4.append(NaN)
        continue

# write all profile p1, p2, p3, p4 point to CSV
with open('allProfilePlot.csv', 'w', newline='') as csvfile:
    fieldnames = ['PX1', 'PY1', 'PX2', 'PY2', 'PX3', 'PY3', 'PX4', 'PY4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x1, x2, x3, x4, y1, y2, y3, y4 in zip(px1, px2, px3, px4, py1, py2, py3, py4):
        writer.writerow({'PX1': '' + str(x1), 'PY1': '' + str(y1), 'PX2': '' + str(x2), 'PY2': '' + str(y2),
                         'PX3': '' + str(x3), 'PY3': '' + str(y3), 'PX4': '' + str(x4), 'PY4': '' + str(y4)})
