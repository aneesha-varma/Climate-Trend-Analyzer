def add_rolling_mean(df):
    df['Rolling_Mean'] = df['Temperature'].rolling(window=12).mean()
    return df

def plot_rolling(df):
    import matplotlib.pyplot as plt
    import os

    os.makedirs("outputs/graphs", exist_ok=True)

    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'], label='Original')
    plt.plot(df['Date'], df['Rolling_Mean'], label='Rolling Mean')

    plt.legend()
    plt.savefig("outputs/graphs/rolling.png")
    plt.show()