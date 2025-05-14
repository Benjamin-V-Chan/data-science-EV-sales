import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    df = pd.read_csv('data/processed/feature_data.csv')
    features = ['Battery_Capacity_kWh', 'Discount_Percentage', 'Units_Sold']
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    kmeans = KMeans(n_clusters=4, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    df.to_csv('outputs/customer_segments.csv', index=False)
    print('Customer segments saved; centroids:')
    print(kmeans.cluster_centers_)

if __name__ == '__main__':
    main()
