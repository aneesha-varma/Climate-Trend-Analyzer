import matplotlib.pyplot as plt

def plot_trend(df):
    plt.figure()
    plt.plot(df['Date'], df['Temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature")

    # ✅ FIXED PATH (NO graphs folder)
    plt.savefig("outputs/temp_trend.png")

    plt.close()