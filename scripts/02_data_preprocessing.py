import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna(subset=['Date', 'Region', 'Brand'])
    for col in ['Battery_Capacity_kWh', 'Discount_Percentage']:
        df[col] = df[col].fillna(df[col].median())
    return df

def main():
    df = pd.read_csv('data/processed/raw_data.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('data/processed/clean_data.csv', index=False)
    print('Cleaned data saved to data/processed/clean_data.csv')

if __name__ == '__main__':
    main()
