import matplotlib.pyplot as plt
import pandas as pd

# only use with original record
for i in range(1, 12884):

    # 118.0 185.0 is median of p1 and p4 point
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    df = df.iloc[51:253]
    df.to_csv('profile_no1_data/profile' + str(i) + '.csv', index=False)