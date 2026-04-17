def detect_anomalies(df):
    import numpy as np

    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = abs(df['Temperature'] - mean) > 2 * std
    return df

def plot_anomalies(df):
    import matplotlib.pyplot as plt
    import os

    os.makedirs("outputs/graphs", exist_ok=True)

    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'])

    plt.scatter(df[df['Anomaly']]['Date'],
                df[df['Anomaly']]['Temperature'],
                color='red')

    plt.savefig("outputs/graphs/anomalies.png")
    plt.show()