import pandas as pd

def add_datetime_features(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year']  = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

def add_discount_flag(df):
    df['Has_Discount'] = (df['Discount_Percentage'] > 0).astype(int)
    return df

def main():
    df = pd.read_csv('data/processed/clean_data.csv')
    df = add_datetime_features(df)
    df = add_discount_flag(df)
    df = pd.get_dummies(df, columns=[
        'Region', 'Brand', 'Vehicle_Type', 
        'Customer_Segment', 'Fast_Charging_Option'
    ], drop_first=True)
    df.to_csv('data/processed/feature_data.csv', index=False)
    print('Feature data saved to data/processed/feature_data.csv')

if __name__ == '__main__':
    main()
