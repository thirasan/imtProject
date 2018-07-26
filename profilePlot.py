import matplotlib.pyplot as plt
import pandas as pd


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


plt.rcParams.update({'figure.max_open_warning': 0})
dfPoint = pd.read_csv('allProfilePlot.csv')

for i in range(1, 1705):
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
        # draw significant point with black color
        plt.plot(dfPoint.iloc[i].PX2, dfPoint.iloc[i].PY2, 'ro', markersize=1, color='black')
        plt.plot(dfPoint.iloc[i].PX3, dfPoint.iloc[i].PY3, 'ro', markersize=1, color='black')
        plt.plot(dfPoint.iloc[i].PX1, dfPoint.iloc[i].PY1, 'ro', markersize=1, color='black')
        plt.plot(dfPoint.iloc[i].PX4, dfPoint.iloc[i].PY4, 'ro', markersize=1, color='black')
        plt.text(dfPoint.iloc[i].PX2 - 2.5, dfPoint.iloc[i].PY2 + 0.5, r'P2', fontsize=8)
        plt.text(dfPoint.iloc[i].PX3 + 0.5, dfPoint.iloc[i].PY3 + 0.5, r'P3', fontsize=8)
        plt.text(dfPoint.iloc[i].PX1 - 2.5, dfPoint.iloc[i].PY1 + 0.5, r'P1', fontsize=8)
        plt.text(dfPoint.iloc[i].PX4 + 0.5, dfPoint.iloc[i].PX4 + 0.5, r'P4', fontsize=8)

    except:
        print("Error with file" + str(i))
        plt.savefig('figureError/figure' + str(i) + '.png')
        continue

    plt.savefig('figure/figure' + str(i) + '.png')
