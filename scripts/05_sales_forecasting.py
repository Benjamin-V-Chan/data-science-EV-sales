import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

def main():
    df = pd.read_csv('data/processed/feature_data.csv')
    X = df.drop(['Units_Sold', 'Revenue', 'Date'], axis=1)
    y = df['Units_Sold']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print(f'Mean Absolute Error: {mae:.2f}')
    joblib.dump(model, 'outputs/sales_forecast_model.pkl')

if __name__ == '__main__':
    main()
