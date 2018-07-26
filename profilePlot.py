import matplotlib.pyplot as plt
import pandas as pd


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
        localAverage = mean([df.loc[currentPoint].Y, df.loc[currentPoint - 1].Y, df.loc[currentPoint - 2].Y,
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
        localAverage = mean([df.loc[currentPoint].Y, df.loc[currentPoint + 1].Y, df.loc[currentPoint + 2].Y,
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


plt.rcParams.update({'figure.max_open_warning': 0})

# loop for range of profile that you need to plot
for i in range(1, 100):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    # saturation variable contain only 254 value\
    saturation = df.loc[df['Intensity'] > 253]

    plt.figure(i)
    plt.suptitle('Profile' + str(i), fontsize=14, fontweight='bold')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    # plot every point
    plt.plot(df.X, df.Y, 'ro', markersize=1, color='red')
    plt.plot(df.X, df.Intensity, 'ro', markersize=1, color='blue')

    try:
        # call function to find significant point
        index_of_p2, p2 = p2Detect(df)
        index_of_p3, p3 = p3Detect(df)
        index_of_p1, p1 = p1Detect(df, index_of_p2)
        index_of_p4, p4 = p4Detect(df, index_of_p3)

        # draw significant point with black color
        plt.plot(p2.X, p2.Y, 'ro', markersize=1, color='black')
        plt.plot(p3.X, p3.Y, 'ro', markersize=1, color='black')
        plt.plot(p1.X, p1.Y, 'ro', markersize=1, color='black')
        plt.plot(p4.X, p4.Y, 'ro', markersize=1, color='black')
        plt.text(p2.X - 2.5, p2.Y + 0.5, r'P2', fontsize=8)
        plt.text(p3.X + 0.5, p3.Y + 0.5, r'P3', fontsize=8)
        plt.text(p1.X - 2.5, p1.Y + 0.5, r'P1', fontsize=8)
        plt.text(p4.X + 0.5, p4.Y + 0.5, r'P4', fontsize=8)

    except:
        # if cannot plot p1, p2, p3, p4 point plot with no them and put in error figure
        print("Error with file" + str(i))
        plt.savefig('figureError/figure' + str(i) + '.png')
        continue

    plt.savefig('figure/figure' + str(i) + '.png')
