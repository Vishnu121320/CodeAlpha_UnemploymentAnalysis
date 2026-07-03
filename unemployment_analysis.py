import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Create Graph Folder
# -----------------------------
os.makedirs("graphs", exist_ok=True)

# -----------------------------
# Load Datasets
# -----------------------------
df1 = pd.read_csv("Unemployment in India.csv")
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Remove extra spaces from column names
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

print("=" * 60)
print("UNEMPLOYMENT ANALYSIS PROJECT")
print("=" * 60)

# -----------------------------
# Dataset 1 Information
# -----------------------------
print("\nDATASET 1")
print("-" * 40)

print("\nFirst 5 Rows")
print(df1.head())

print("\nShape")
print(df1.shape)

print("\nInfo")
print(df1.info())

print("\nMissing Values")
print(df1.isnull().sum())

print("\nSummary Statistics")
print(df1.describe())

# -----------------------------
# Dataset 2 Information
# -----------------------------
print("\nDATASET 2")
print("-" * 40)

print("\nFirst 5 Rows")
print(df2.head())

print("\nShape")
print(df2.shape)

print("\nInfo")
print(df2.info())

print("\nMissing Values")
print(df2.isnull().sum())

print("\nSummary Statistics")
print(df2.describe())

# -----------------------------
# Convert Date Columns
# -----------------------------
df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)
df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)

# -----------------------------
# GRAPH 1
# Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df1["Estimated Unemployment Rate (%)"],
             bins=20,
             kde=True,
             color="blue")
plt.title("Distribution of Unemployment Rate")
plt.savefig("graphs/unemployment_distribution.png")
plt.close()

# -----------------------------
# GRAPH 2
# State Wise Average
# -----------------------------
plt.figure(figsize=(12,8))

state_avg = df1.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values()

state_avg.plot(kind="barh")

plt.xlabel("Average Unemployment Rate")
plt.title("State-wise Average Unemployment")
plt.tight_layout()

plt.savefig("graphs/statewise_unemployment.png")
plt.close()

# -----------------------------
# GRAPH 3
# Rural vs Urban
# -----------------------------
plt.figure(figsize=(7,5))

sns.boxplot(
    x="Area",
    y="Estimated Unemployment Rate (%)",
    data=df1
)

plt.title("Rural vs Urban Unemployment")

plt.savefig("graphs/rural_vs_urban.png")
plt.close()

# -----------------------------
# GRAPH 4
# Monthly Trend
# -----------------------------
monthly = df1.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(12,5))

plt.plot(monthly.index,
         monthly.values,
         marker="o")

plt.title("Monthly Unemployment Trend")

plt.xlabel("Date")
plt.ylabel("Average Rate")

plt.grid()

plt.savefig("graphs/monthly_trend.png")
plt.close()

# -----------------------------
# GRAPH 5
# Covid Impact
# -----------------------------
covid = df1[df1["Date"] >= "2020-03-01"]

monthly2 = covid.groupby("Date")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(10,5))

plt.plot(monthly2.index,
         monthly2.values,
         marker="o",
         color="red")

plt.title("Covid-19 Impact on Unemployment")

plt.grid()

plt.savefig("graphs/covid_impact.png")
plt.close()

# -----------------------------
# GRAPH 6
# Region Analysis
# -----------------------------
plt.figure(figsize=(8,6))

region_avg = df2.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

region_avg.plot(kind="bar", color="orange")

plt.ylabel("Average Rate")

plt.title("Region-wise Average Unemployment")

plt.tight_layout()

plt.savefig("graphs/regional_analysis.png")
plt.close()

# -----------------------------
# GRAPH 7
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(7,6))

corr = df2.select_dtypes(include="number").corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")

plt.savefig("graphs/correlation_heatmap.png")
plt.close()

# -----------------------------
# GRAPH 8
# Box Plot
# -----------------------------
plt.figure(figsize=(8,5))

sns.boxplot(
    y=df1["Estimated Unemployment Rate (%)"],
    color="skyblue"
)

plt.title("Box Plot of Unemployment Rate")

plt.savefig("graphs/boxplot.png")
plt.close()

# -----------------------------
# GRAPH 9
# Top 10 States
# -----------------------------
top10 = state_avg.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))

top10.plot(kind="bar", color="green")

plt.title("Top 10 Highest Unemployment States")

plt.ylabel("Average Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("graphs/top10_states.png")
plt.close()

# -----------------------------
# Insights
# -----------------------------
highest_state = state_avg.idxmax()
lowest_state = state_avg.idxmin()

highest_rate = state_avg.max()
lowest_rate = state_avg.min()

average_rate = df1["Estimated Unemployment Rate (%)"].mean()

print("\n")
print("=" * 60)
print("PROJECT INSIGHTS")
print("=" * 60)

print(f"Average Unemployment Rate : {average_rate:.2f}%")

print(f"\nHighest Unemployment State : {highest_state}")
print(f"Rate : {highest_rate:.2f}%")

print(f"\nLowest Unemployment State : {lowest_state}")
print(f"Rate : {lowest_rate:.2f}%")

print("\nCovid-19 Observation:")
print("Unemployment increased significantly during April and May 2020.")

print("\nGraphs saved successfully inside the 'graphs' folder.")

print("\nProject Completed Successfully.")