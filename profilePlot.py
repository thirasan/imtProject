import matplotlib.pyplot as plt
import pandas as pd


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


plt.rcParams.update({'figure.max_open_warning': 0})

for i in range(4930, 5031):
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    saturation = df.loc[df['Intensity'] > 253]

    plt.figure(i)
    plt.suptitle('Profile' + str(i), fontsize=14, fontweight='bold')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')

    plt.plot(df.X, df.Y, 'ro', markersize=1, color='red')
    plt.plot(df.X, df.Intensity, 'ro', markersize=1, color='blue')

    try:
        pointer = 0
        while True:
            if saturation.iloc[0 + pointer].Y > mean(list(saturation.Y)) - 5.0:
                index_of_p2 = saturation.index[0 + pointer] - 1
                p2 = df.loc[index_of_p2]
                break
            else:
                pointer += 1
                continue

        pointer = 0
        while True:
            if saturation.iloc[-(1 + pointer)].Y > mean(list(saturation.Y)) - 5.0:
                index_of_p3 = saturation.index[-(1 + pointer)] + 1
                p3 = df.loc[index_of_p3]
                break
            else:
                pointer += 1
                continue

        while True:
            localMean = mean([df.loc[index_of_p2].Y, df.loc[index_of_p2 - 1].Y, df.loc[index_of_p2 - 2].Y
                                 , df.loc[index_of_p2 - 3].Y, df.loc[index_of_p2 - 4].Y])
            if localMean + 0.1 > df.loc[index_of_p2].Y > localMean - 0.1:
                p1 = df.loc[index_of_p2]
                break
            elif index_of_p2 <= 5:
                break
            else:
                index_of_p2 -= 1
                continue

        while True:
            localMean = mean([df.loc[index_of_p3].Y, df.loc[index_of_p3 + 1].Y, df.loc[index_of_p3 + 2].Y
                                 , df.loc[index_of_p3 + 3].Y, df.loc[index_of_p3 + 4].Y])
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


