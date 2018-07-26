from json.decoder import NaN

import matplotlib.pyplot as plt
import pandas as pd
import csv


# function which return average number
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def p2Detect(df):
    # Find p2 point by identified the first saturation point
    pointer = 0
    while True:
        if saturation.iloc[0 + pointer].Y > mean(list(saturation.Y)) - 0.2:
            index_of_p2 = saturation.index[0 + pointer]
            localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 + 1].Y, df.loc[index_of_p2 + 2].Y, df.loc[index_of_p2 + 3].Y,
                              df.loc[index_of_p2 + 4].Y])
            while localMean + 1.5 > df.loc[index_of_p2].Y > localMean - 1.5:
                if index_of_p2 < 10:
                    # index_of_p2 = saturation.index[0 + pointer]
                    break
                index_of_p2 -= 1
            return index_of_p2, df.loc[index_of_p2]
            break
        else:
            pointer += 1
            continue


def p3Detect(df):
    # Find p3 point by identified the last saturation point
    pointer = 0
    while True:
        if saturation.iloc[-(1 + pointer)].Y > mean(list(saturation.Y)) - 0.2:
            index_of_p3 = saturation.index[-(1 + pointer)]
            localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 - 1].Y, df.loc[index_of_p3 - 2].Y, df.loc[index_of_p3 - 3].Y,
                              df.loc[index_of_p3 - 4].Y])
            while localMean + 1.5 > df.loc[index_of_p3].Y > localMean - 1.5:
                if index_of_p3 > len(df.index) - 10:
                    index_of_p3 -= 1
                    # index_of_p3 = saturation.index[-(1 + pointer)]
                    break
                index_of_p3 += 1
            return index_of_p3, df.loc[index_of_p3]
            break
        else:
            pointer += 1
            continue


def p1Detect(df, index_of_p2):
    # Find the p1 point by find local mean according to p2 point
    while True:
        localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 - 1].Y, df.loc[index_of_p2 - 2].Y,
                          df.loc[index_of_p2 - 3].Y, df.loc[index_of_p2 - 4].Y, df.loc[index_of_p2 - 5].Y])

        p1 = df.loc[index_of_p2]
        if localMean + 0.5 > df.loc[index_of_p2].Y > localMean - 0.5:
            for k in range(1, 6):
                temp = mean([df.loc[index_of_p2 + k].Y, df.loc[index_of_p2 - 1 + k].Y,
                                  df.loc[index_of_p2 - 2 + k].Y, df.loc[index_of_p2 - 3 + k].Y,
                                  df.loc[index_of_p2 - 4 + k].Y, df.loc[index_of_p2 - 5 + k].Y])
                if temp + 0.5 > df.loc[index_of_p2 + k].Y > temp - 0.5:
                    check = True
                    continue
                else:
                    check = False
                    break

            if check is False:
                index_of_p2 -= 1
                continue

            return index_of_p2, p1
            break
        elif index_of_p2 <= 11:
            break
        else:
            index_of_p2 -= 1
            continue


def p4Detect(df, index_of_p3):
    # Find the p4 point by find local mean according to p3 point
    while True:
        localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 + 1].Y, df.loc[index_of_p3 + 2].Y,
                          df.loc[index_of_p3 + 3].Y, df.loc[index_of_p3 + 4].Y, df.loc[index_of_p3 + 5].Y])

        p4 = df.loc[index_of_p3]
        if localMean + 0.5 > df.loc[index_of_p3].Y > localMean - 0.5:
            for k in range(1, 6):
                temp = mean([df.loc[index_of_p3 + k].Y, df.loc[index_of_p3 + 1 + k].Y, df.loc[index_of_p3 + 2 + k].Y,
                             df.loc[index_of_p3 + 3 + k].Y, df.loc[index_of_p3 + 4 + k].Y, df.loc[index_of_p3 + 5 + k].Y])
                if temp + 0.5 > df.loc[index_of_p3 + k].Y > temp - 0.5:
                    check = True
                    continue
                else:
                    check = False
                    break

            if check is False:
                index_of_p3 += 1
                continue

            return index_of_p3, p4
            break
        elif index_of_p3 >= len(df.index) - 11:
            break
        else:
            index_of_p3 += 1
            continue


px1 = list()
px2 = list()
px3 = list()
px4 = list()

py1 = list()
py2 = list()
py3 = list()
py4 = list()

for i in range(1, 1705):
    try:
        df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
        # saturation variable contain only 254 value
        saturation = df.loc[df['Intensity'] > 253]

        # 12884
        index_of_p2, p2 = p2Detect(df)
        index_of_p3, p3 = p3Detect(df)
        inp1, p1 = p1Detect(df, index_of_p2)
        inp2, p4 = p4Detect(df, index_of_p3)

        # add axis of p1-p4 to variable
        px1.append(p1.X)
        px2.append(p2.X)
        px3.append(p3.X)
        px4.append(p4.X)

        py1.append(p1.Y)
        py2.append(p2.Y)
        py3.append(p3.Y)
        py4.append(p4.Y)

        # add index of p1-p4 to variable
        # pa1.append(inp1)
        # pa2.append(inp2)
        # pa3.append(inp3)
        # pa4.append(inp4)
    except:
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

# write all profile to CSV
with open('allProfilePlot.csv', 'w', newline='') as csvfile:
    fieldnames = ['PX1', 'PY1', 'PX2', 'PY2', 'PX3', 'PY3', 'PX4', 'PY4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for x1, x2, x3, x4, y1, y2, y3, y4 in zip(px1, px2, px3, px4, py1, py2, py3, py4):
        writer.writerow({'PX1': '' + str(x1), 'PY1': '' + str(y1), 'PX2': '' + str(x2), 'PY2': '' + str(y2),
                         'PX3': '' + str(x3), 'PY3': '' + str(y3), 'PX4': '' + str(x4), 'PY4': '' + str(y4)})
