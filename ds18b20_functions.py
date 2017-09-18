import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def get_data(file_name):
    # Get data from ds18b20.log file
    df = pd.read_csv(file_name, names=['Date', 'Temp'], header=None, sep=' ')
    df['Date'] = [dt.datetime.strptime(datestr, '%Y-%m-%d_%H:%M:%S') for datestr in df['Date']]
    df['Temp'] = df['Temp'] / 1000.
    df.index=df['Date']
    return df


def clean_up_data(df):
    # Clean up data with error reading of 85.0
    temps = np.array(df['Temp'])
    if temps[0] == 85.:
        temps[0] = temps[1]
    if temps[-1] == 85.:
        temps[-1] = temps[-2]
    for i in range(len(temps)):
        if temps[i] == 85.:
            temps[i] = np.mean([temps[i - 1], temps[i + 1]])
    df['Temp'] = temps

