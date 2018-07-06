import matplotlib.pyplot as plt
import pandas as pd


for i in range(1, 12884):

    # 118.0 185.0 is median of p1 and p4 point
    df = pd.read_csv('profile_no1_data/profile' + str(i) + '.csv')
    df = df.iloc[51:253]
    df.to_csv('new_profile_no1_data/profile' + str(i) + '.csv', index=False)