import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('outputs/customer_segments.csv')

    yearly = df.groupby('Year')['Units_Sold'].sum()
    plt.figure()
    yearly.plot()
    plt.title('Yearly Sales Trend')
    plt.savefig('outputs/yearly_sales_trend.png')

    plt.figure()
    plt.scatter(df['Battery_Capacity_kWh'], df['Units_Sold'])
    plt.title('Battery Capacity vs Units Sold')
    plt.savefig('outputs/battery_vs_sales.png')

    counts = df['Cluster'].value_counts().sort_index()
    plt.figure()
    counts.plot(kind='bar')
    plt.title('Cluster Distribution')
    plt.savefig('outputs/cluster_distribution.png')

    print('Visualizations saved to outputs/')

if __name__ == '__main__':
    main()
