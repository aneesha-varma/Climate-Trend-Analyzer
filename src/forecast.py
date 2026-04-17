from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import os

def forecast_temp(df):
    df['Year'] = df['Date'].dt.year

    X = df[['Year']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    future_years = np.arange(2025, 2035).reshape(-1,1)
    predictions = model.predict(future_years)

    return future_years.flatten(), predictions


def plot_forecast(df, future_years, predictions):
    os.makedirs("outputs/graphs", exist_ok=True)

    plt.figure(figsize=(10,5))
    plt.plot(df['Date'].dt.year, df['Temperature'], label='Actual')
    plt.plot(future_years, predictions, label='Forecast', color='red')

    plt.legend()
    plt.grid()

    plt.savefig("outputs/graphs/forecast.png")
    plt.show()