import pandas as pd
import os

def load_and_combine():
    df_train = pd.read_csv('data/raw/train.csv')
    df_test  = pd.read_csv('data/raw/test.csv')
    return pd.concat([df_train, df_test], sort=False)

def main():
    os.makedirs('data/processed', exist_ok=True)
    df = load_and_combine()
    df.to_csv('data/processed/raw_data.csv', index=False)
    print(f'Raw data saved: {df.shape[0]} rows, {df.shape[1]} columns')

if __name__ == '__main__':
    main()
