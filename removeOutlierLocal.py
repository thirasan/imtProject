import matplotlib.pyplot as plt
import pandas as pd
import csv

df_median_profile = pd.read_csv('localMedian/medianProfile1-100.csv')
df_mad = pd.read_csv('localMAD/mad1-100.csv')
dfPrevious = df_median_profile

plt.rcParams.update({'figure.max_open_warning': 0})

for i in range(1, 12884):
    try:
        if i % 100 == 0:
            df_median_profile = pd.read_csv('localMedian/medianProfile' + str(i) + "-" + str(i+100) + '.csv')
            df_mad = pd.read_csv('localMAD/mad' + str(i) + "-" + str(i + 100) + '.csv')
    except:
        df_median_profile = pd.read_csv('localMedian/medianProfile' + str(i) + '-12883.csv')
        df_mad = pd.read_csv('localMAD/mad' + str(i) + '-12883.csv')

    x = list()
    y = list()
    intensity = list()

    # if i > 1:
    #     dfPrevious = pd.read_csv('profile_no1_data/profile' + str(i - 1) + '.csv')
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')

    for row, rangeMad, medianPro in zip(df.iterrows(), df_mad.iterrows(), df_median_profile.iterrows()):
        x.append(row[1].X)
        intensity.append(row[1].Intensity)
        if rangeMad[1].MAD_Top <= row[1].Y <= rangeMad[1].MAD_Bottom:
            y.append(row[1].Y)
        else:
            y.append(medianPro[1].Y)
    with open('profile_no1_data/profile' + str(i) + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['X', 'Y', 'Intensity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for a, j, k in zip(x, y, intensity):
            writer.writerow({'X': '' + str(a), 'Y': '' + str(j), 'Intensity': '' + str(k)})

    # plt.figure(i)
    # plt.suptitle('medianRange', fontsize=14, fontweight='bold')
    # plt.xlabel('X axis')
    # plt.ylabel('Y axis')
    #
    # plt.plot(df.X, df.Y, 'ro', markersize=1, color='red')
    # plt.plot(df.X, df.Intensity, 'ro', markersize=1, color='blue')
    # plt.plot(df.X, df_mad.MAD_Top, 'ro', markersize=1, color='greenyellow')
    # plt.plot(df.X, df_mad.MAD_Bottom, 'ro', markersize=1, color='greenyellow')
    # plt.savefig('figureSample/figureSample' + str(i) + '.png')


    # plt.show()
