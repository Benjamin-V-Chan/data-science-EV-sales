import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/processed/feature_data.csv')
    df.describe(include='all').to_csv('outputs/eda_summary.csv')

    region_sales = df.groupby('Region')['Units_Sold'].sum().reset_index()
    region_sales.to_csv('outputs/region_sales_summary.csv', index=False)

    brand_revenue = df.groupby('Brand')['Revenue'].mean().reset_index()
    brand_revenue.to_csv('outputs/brand_revenue_summary.csv', index=False)

    plt.figure()
    region_sales.plot.bar(x='Region', y='Units_Sold', legend=False)
    plt.title('Units Sold by Region')
    plt.savefig('outputs/units_by_region.png')

    plt.figure()
    df.groupby('Date')['Units_Sold'].sum().plot()
    plt.title('Monthly Sales Trend')
    plt.savefig('outputs/sales_trend.png')

    print('EDA outputs saved to outputs/')
    
if __name__ == '__main__':
    main()
