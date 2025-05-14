# data-science-EV-sales

## Project Overview

This project performs a comprehensive data science workflow on electric vehicle (EV) sales and adoption data. It includes preprocessing, feature engineering, exploratory data analysis, market segmentation, forecasting, and reporting. The objective is to derive insights for business strategy, identify key market segments, and predict future EV sales using machine learning models.

## Folder Structure

```
project-root/
├── data/
│   ├── raw/                 # Original dataset files (train.csv, test.csv)
│   ├── processed/           # Cleaned and feature-enhanced versions of the data
├── outputs/                 # Model files, plots, analysis reports
├── scripts/                 # Python scripts for all stages of analysis
│   ├── 01_data_ingestion.py
│   ├── 02_data_preprocessing.py
│   ├── 03_feature_engineering.py
│   ├── 04_exploratory_analysis.py
│   ├── 05_sales_forecasting.py
│   ├── 06_segmentation_analysis.py
│   └── 07_visualization_reports.py
├── requirements.txt         # Python dependencies
└── README.md                # Project overview and instructions
```

## Usage

1. **Setup the Project:**

   * Clone the repository.
   * Ensure you have Python installed.
   * Install required dependencies using the requirements.txt file.

     ```bash
     pip install -r requirements.txt
     ```

2. **Ingest and Combine Raw Data:**

   ```bash
   python scripts/01_data_ingestion.py
   ```

3. **Clean and Preprocess Data:**

   ```bash
   python scripts/02_data_preprocessing.py
   ```

4. **Perform Feature Engineering:**

   ```bash
   python scripts/03_feature_engineering.py
   ```

5. **Run Exploratory Data Analysis:**

   ```bash
   python scripts/04_exploratory_analysis.py
   ```

6. **Train Sales Forecasting Model:**

   ```bash
   python scripts/05_sales_forecasting.py
   ```

7. **Run Market Segmentation Analysis:**

   ```bash
   python scripts/06_segmentation_analysis.py
   ```

8. **Generate Visual Reports:**

   ```bash
   python scripts/07_visualization_reports.py
   ```

## Requirements

The project uses the following Python packages:

* pandas
* numpy
* matplotlib
* scikit-learn
* joblib

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Acknowledgments

**Dataset Name:** Electric Vehicle (EV) Sales and Adoption 🌍🚗⚡
**Dataset Author:** Rameez Meerasahib
**Dataset Source:** [https://www.kaggle.com/datasets/rameezmeerasahib/electric-vehicle-ev-sales-and-adoption](https://www.kaggle.com/datasets/rameezmeerasahib/electric-vehicle-ev-sales-and-adoption)
