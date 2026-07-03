# 📊 Unemployment Analysis with Python

## 📌 Project Overview

This project is developed as part of the **CodeAlpha Data Science Internship**.

The objective of this project is to analyze unemployment trends in India using Python. The analysis includes data cleaning, exploratory data analysis (EDA), visualization, and insights into unemployment patterns before and during the COVID-19 pandemic.

## 📂 Dataset

The project uses two datasets:

- Unemployment in India.csv
- Unemployment_Rate_upto_11_2020.csv

The datasets contain information such as:

- Region (State)
- Date
- Frequency
- Estimated Unemployment Rate (%)
- Estimated Employed
- Estimated Labour Participation Rate (%)
- Area (Rural/Urban)
- Region Category
- Latitude
- Longitude

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📈 Features

- Load and analyze unemployment datasets
- Data cleaning and preprocessing
- Missing value analysis
- Summary statistics
- State-wise unemployment analysis
- Rural vs Urban unemployment comparison
- Monthly unemployment trend
- COVID-19 unemployment impact analysis
- Regional unemployment comparison
- Correlation analysis
- Automatic graph generation and saving
- Project insights generation

## 📊 Graphs Generated

The project automatically generates and saves the following graphs:

- Unemployment Distribution
- State-wise Average Unemployment
- Rural vs Urban Comparison
- Monthly Trend
- COVID-19 Impact
- Region-wise Analysis
- Correlation Heatmap
- Box Plot
- Top 10 Highest Unemployment States

All graphs are stored inside the **graphs/** folder.

## 📁 Project Structure

```text
CodeAlpha_UnemploymentAnalysis
│
├── graphs
│   ├── unemployment_distribution.png
│   ├── statewise_unemployment.png
│   ├── rural_vs_urban.png
│   ├── monthly_trend.png
│   ├── covid_impact.png
│   ├── regional_analysis.png
│   ├── correlation_heatmap.png
│   ├── boxplot.png
│   └── top10_states.png
│
├── unemployment_analysis.py
├── Unemployment in India.csv
├── Unemployment_Rate_upto_11_2020.csv
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_UnemploymentAnalysis.git
```

### Open the project folder

```bash
cd CodeAlpha_UnemploymentAnalysis
```

### Install required libraries

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python unemployment_analysis.py
```

## 📌 Sample Output

```text
Average Unemployment Rate : 11.79%

Highest Unemployment State :
Tripura

Rate : 28.35%

Lowest Unemployment State :
Meghalaya

Rate : 4.80%

Graphs saved successfully inside the graphs folder.

Project Completed Successfully.
```

## 📊 Key Insights

- Tripura recorded the highest average unemployment rate.
- Meghalaya recorded the lowest average unemployment rate.
- Unemployment increased significantly during April and May 2020 due to the COVID-19 lockdown.
- Rural and Urban unemployment trends vary across different states.
- Regional analysis helps compare unemployment across different parts of India.

## 🎯 Future Improvements

- Interactive Dashboard using Streamlit
- Power BI Dashboard
- Predictive unemployment forecasting using Machine Learning
- State-wise interactive maps
- Time-series forecasting using ARIMA/LSTM

## 👨‍💻 Author

**Vishnu Teja Chennuru**
