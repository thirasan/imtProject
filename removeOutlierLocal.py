import matplotlib.pyplot as plt
import pandas as pd
import csv

# variable for choose range of local profiles
localRange = 100

# variable for track last profile
lastPosition = 12883

# load first local MAD and median
df_median_profile = pd.read_csv('localMedian/medianProfile1-' + str(localRange) + '.csv')
df_mad = pd.read_csv('localMAD/mad1-' + str(localRange) + '.csv')

plt.rcParams.update({'figure.max_open_warning': 0})

for i in range(1, lastPosition + 1):

    # if reach then next range change local MAD and median
    try:
        if i % localRange == 0:
            df_median_profile = pd.read_csv('localMedian/medianProfile' + str(i) + "-" + str(i + localRange) + '.csv')
            df_mad = pd.read_csv('localMAD/mad' + str(i) + "-" + str(i + localRange) + '.csv')
    except:
        # if profile is reach the last range change MAD and median profile to the last one
        df_median_profile = pd.read_csv('localMedian/medianProfile' + str(i) + '-' + str(lastPosition) + '.csv')
        df_mad = pd.read_csv('localMAD/mad' + str(i) + '-' + str(lastPosition) + '.csv')

    # variables to store the new profile
    x = list()
    y = list()
    intensity = list()

    # load current profile
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')

    # loop for all index in profile
    for row, rangeMad, medianPro in zip(df.iterrows(), df_mad.iterrows(), df_median_profile.iterrows()):
        # keep original intensity
        intensity.append(row[1].Intensity)

        # if current index is in MAD range fill with index of original profile
        if rangeMad[1].MAD_Bottom <= row[1].Y <= rangeMad[1].MAD_Top:
            x.append(row[1].X)
            y.append(row[1].Y)
        # if not fill with index of median profile
        else:
            x.append(medianPro[1].X)
            y.append(medianPro[1].Y)

    # write new profile
    with open('profile_no1_data/profile' + str(i) + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['X', 'Y', 'Intensity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for a, j, k in zip(x, y, intensity):
            writer.writerow({'X': '' + str(a), 'Y': '' + str(j), 'Intensity': '' + str(k)})
