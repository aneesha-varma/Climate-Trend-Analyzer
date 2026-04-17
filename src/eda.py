import matplotlib.pyplot as plt

def plot_trend(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'])
    plt.title("Temperature Trend")
    plt.savefig("outputs/graphs/temp_trend.png")
    plt.show()