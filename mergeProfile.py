import matplotlib.pyplot as plt
import pandas as pd
import csv


# function which return average number
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


pa1 = list()
pa2 = list()
pa3 = list()
pa4 = list()

for i in range(1, 12884):
    try:
        df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
        # saturation variable contain only 254 value
        saturation = df.loc[df['Intensity'] > 253]

        # 12884
        # Find p2 point by identified the first saturation point
        pointer = 0
        while True:
            if saturation.iloc[0 + pointer].Y > mean(list(saturation.Y)) - 0.2:
                temp = saturation.index[0 + pointer]
                localMean = mean([df.loc[temp].Y, df.loc[temp + 1].Y, df.loc[temp + 2].Y, df.loc[temp + 3].Y,
                                  df.loc[temp + 4].Y])
                while localMean + 1.5 > df.loc[temp].Y > localMean - 1.5:
                    if temp < 10:
                        # temp = saturation.index[0 + pointer]
                        break
                    temp -= 1
                index_of_p2 = temp
                p2 = df.loc[index_of_p2]
                inp2 = index_of_p2
                break
            else:
                pointer += 1
                continue

        # Find p3 point by identified the last saturation point
        pointer = 0
        while True:
            if saturation.iloc[-(1 + pointer)].Y > mean(list(saturation.Y)) - 0.2:
                temp = saturation.index[-(1 + pointer)]
                localMean = mean([df.loc[temp].Y, df.loc[temp - 1].Y, df.loc[temp - 2].Y, df.loc[temp - 3].Y,
                                  df.loc[temp - 4].Y])
                while localMean + 1.5 > df.loc[temp].Y > localMean - 1.5:
                    if temp > len(df.index) - 10:
                        temp -= 1
                        # temp = saturation.index[-(1 + pointer)]
                        break
                    temp += 1
                index_of_p3 = temp
                p3 = df.loc[index_of_p3]
                inp3 = index_of_p3
                break
            else:
                pointer += 1
                continue

        # Find the p1 point by find local mean according to p2 point
        while True:
            localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 - 1].Y, df.loc[index_of_p2 - 2].Y,
                              df.loc[index_of_p2 - 3].Y, df.loc[index_of_p2 - 4].Y, df.loc[index_of_p2 - 5].Y])

            p1 = df.loc[index_of_p2]
            if localMean + 0.5 > df.loc[index_of_p2].Y > localMean - 0.5:
                if p2.X - p1.X < 4.5:
                    index_of_p2 -= 1
                    continue
                inp1 = index_of_p2
                break
            elif index_of_p2 <= 11:
                break
            else:
                index_of_p2 -= 1
                continue

        # Find the p4 point by find local mean according to p3 point
        while True:
            localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 + 1].Y, df.loc[index_of_p3 + 2].Y,
                              df.loc[index_of_p3 + 3].Y, df.loc[index_of_p3 + 4].Y, df.loc[index_of_p3 + 5].Y])

            p4 = df.loc[index_of_p3]
            if localMean + 0.5 > df.loc[index_of_p3].Y > localMean - 0.5:
                if p4.X - p3.X < 4.5:
                    index_of_p3 += 1
                    continue
                inp4 = index_of_p3
                break
            elif index_of_p3 >= len(df.index) - 11:
                break
            else:
                index_of_p3 += 1
                continue

        # add axis of p1-p4 to variable
        pa1.append(p1.X)
        pa2.append(p2.X)
        pa3.append(p3.X)
        pa4.append(p4.X)

        # add index of p1-p4 to variable
        # pa1.append(inp1)
        # pa2.append(inp2)
        # pa3.append(inp3)
        # pa4.append(inp4)
    except:
        print("Error with file" + str(i))

# write all profile to CSV
with open('allProfilePlot.csv', 'w', newline='') as csvfile:
    fieldnames = ['P1', 'P2', 'P3', 'P4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, j, k, l in zip(pa1, pa2, pa3, pa4):
        writer.writerow({'P1': '' + str(i), 'P2': '' + str(j), 'P3': '' + str(k), 'P4': '' + str(l)})
