import matplotlib.pyplot as plt
import pandas as pd


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


plt.rcParams.update({'figure.max_open_warning': 0})

for i in range(1, 12884):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    saturation = df.loc[df['Intensity'] > 253]

    plt.figure(i)
    plt.suptitle('Profile' + str(i), fontsize=14, fontweight='bold')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    plt.plot(df.X, df.Y, 'ro', markersize=1, color='red')
    plt.plot(df.X, df.Intensity, 'ro', markersize=1, color='blue')

    try:
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

        plt.plot(p2.X, p2.Y, 'ro', markersize=1, color='black')
        plt.plot(p3.X, p3.Y, 'ro', markersize=1, color='black')
        plt.plot(p1.X, p1.Y, 'ro', markersize=1, color='black')
        plt.plot(p4.X, p4.Y, 'ro', markersize=1, color='black')

        plt.text(p2.X - 2.5, p2.Y + 0.5, r'P2', fontsize=8)
        plt.text(p3.X + 0.5, p3.Y + 0.5, r'P3', fontsize=8)
        plt.text(p1.X - 2.5, p1.Y + 0.5, r'P1', fontsize=8)
        plt.text(p4.X + 0.5, p4.Y + 0.5, r'P4', fontsize=8)
    except:
        print("Error with file" + str(i))
        plt.savefig('figureError/figure' + str(i) + '.png')
        continue

    plt.savefig('figure/figure' + str(i) + '.png')
