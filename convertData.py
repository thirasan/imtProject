import csv

# fill with raw data name
with open('003476-av.pro2.csv', newline='') as csvfile:
    spamReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    count = 1

    line = iter(spamReader)
    for row in line:
        parameter = row[0].split('NaN')

        x = parameter[0].split(';')
        y = parameter[1].split(';')
        intensity = parameter[2].split(';')

        x = [item for item in x if item not in ' ']
        y = [item for item in y if item not in ' ']
        intensity = [item for item in intensity if item not in ' ']

        with open('profile_no1_data/profile' + str(count) + '.csv', 'w', newline='') as csvfile:
            fieldnames = ['X', 'Y', 'Intensity']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for i, j, k in zip(x, y, intensity):
                writer.writerow({'X': '' + i, 'Y': '' + j, 'Intensity': '' + k})
        count += 1
