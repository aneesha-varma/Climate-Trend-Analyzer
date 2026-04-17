import pandas as pd

def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')

    df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())

    print("✅ Data Cleaned")
    return df