import matplotlib.pyplot as plt
import pandas as pd
import csv


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


pa1 = list()
pa2 = list()
pa3 = list()
pa4 = list()

for i in range(4000, 4800):
    try:
        df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
        saturation = df.loc[df['Intensity'] > 253]

        # 12884
        pointer = 0
        while True:
            if saturation.iloc[0 + pointer].Y > mean(list(saturation.Y)) - 5.0:
                temp = saturation.index[0 + pointer]
                localMean = mean([df.loc[temp].Y, df.loc[temp + 1].Y, df.loc[temp + 2].Y, df.loc[temp + 3].Y,
                                  df.loc[temp + 4].Y])
                while localMean + 1.5 > df.loc[temp].Y > localMean - 1.5:
                    temp -= 1
                index_of_p2 = temp
                p2 = df.loc[index_of_p2]
                break
            else:
                pointer += 1
                continue

        pointer = 0
        while True:
            if saturation.iloc[-(1 + pointer)].Y > mean(list(saturation.Y)) - 5.0:
                temp = saturation.index[-(1 + pointer)]
                localMean = mean([df.loc[temp].Y, df.loc[temp - 1].Y, df.loc[temp - 2].Y, df.loc[temp - 3].Y,
                                  df.loc[temp - 4].Y])
                while localMean + 1.5 > df.loc[temp].Y > localMean - 1.5:
                    temp += 1
                index_of_p3 = temp
                p3 = df.loc[index_of_p3]
                break
            else:
                pointer += 1
                continue

        while True:
            localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 - 1].Y, df.loc[index_of_p2 - 2].Y,
                              df.loc[index_of_p2 - 3].Y, df.loc[index_of_p2 - 4].Y, df.loc[index_of_p2 - 5].Y,
                             df.loc[index_of_p2 - 6].Y, df.loc[index_of_p2 - 7].Y,df.loc[index_of_p2 - 8].Y,
                             df.loc[index_of_p2 - 9].Y])
            if localMean + 0.1 > df.loc[index_of_p2].Y > localMean - 0.1:
                p1 = df.loc[index_of_p2]
                break
            elif index_of_p2 <= 5:
                break
            else:
                index_of_p2 -= 1
                continue

        while True:
            localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 + 1].Y, df.loc[index_of_p3 + 2].Y,
                              df.loc[index_of_p3 + 3].Y, df.loc[index_of_p3 + 4].Y, df.loc[index_of_p3 + 5].Y,
                             df.loc[index_of_p3 + 6].Y, df.loc[index_of_p3 + 7].Y,
                             df.loc[index_of_p3 + 8].Y, df.loc[index_of_p3 + 9].Y])
            if localMean + 0.1 > df.loc[index_of_p3].Y > localMean - 0.1:
                p4 = df.loc[index_of_p3]
                break
            elif index_of_p3 >= len(df.index) - 5:
                break
            else:
                index_of_p3 += 1
                continue

        pa1.append(p1.X)
        pa2.append(p2.X)
        pa3.append(p3.X)
        pa4.append(p4.X)

    except:
        print("Error with file" + str(i))

with open('allProfilePlot.csv', 'w', newline='') as csvfile:
    fieldnames = ['P1', 'P2', 'P3', 'P4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, j, k, l in zip(pa1, pa2, pa3, pa4):
        writer.writerow({'P1': '' + str(i), 'P2': '' + str(j), 'P3': '' + str(k), 'P4': '' + str(l)})
