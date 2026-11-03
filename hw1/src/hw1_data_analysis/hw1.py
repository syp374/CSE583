
# CSE 583 - Homework 1: Python Data Analysis Basics

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

script_directory = Path(__file__).resolve().parent


# 2. Read the bicycle data CSV file
df = pd.read_csv("/Users/seyoungpark/CSE583-1/hw1/src/hw1_data_analysis/bicycle_data.csv")

print("Dataset dimensions:", df.shape)

# See the actual data
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
print(df.head())


# 3. Describe columns and check data types
# Date: date and time of each observation (datetime).
# Fremont Bridge East Sidewalk: hourly bicycle count (numeric).
# Fremont Bridge West Sidewalk: hourly bicycle count (numeric).

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())


# 4. Convert Date to datetime (Bonus)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")

print("\nUpdated data types:")
print(df.dtypes)


# 5. Add total count, hour, and year columns

east = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"
west = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"

df[east] = pd.to_numeric(df[east], errors="coerce")
df[west] = pd.to_numeric(df[west], errors="coerce")

# Total count is missing if either sidewalk count is missing.
df["Total"] = df[[east, west]].sum(axis=1, min_count=2)

df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

print("\nDataFrame with new columns:")
print(df.head())


# 6. Create a DataFrame containing only 2016 data
df_2016 = df[df["Year"] == 2016].copy()

print("\nNumber of observations in 2016:", len(df_2016))
print("\nFirst five rows of 2016 data:")
print(df_2016.head())


# 7. Check and handle missing data

missing_count = df_2016["Total"].isna().sum()

print("\nNumber of time points with missing bicycle counts:", missing_count)

# Number of 2016 time points with missing bicycle counts: 8784

# Remove observations with missing bicycle counts or hours.
df_2016 = df_2016.dropna(subset=["Total", "Hour"])


# 8. Calculate average bicycle counts by hour

hourly_average = df_2016.groupby("Hour")["Total"].mean()

print("\nAverage bicycle count by hour:")
print(hourly_average)


# 9. Plot average bicycle counts by hour

plt.figure(figsize=(10, 6))

plt.plot(hourly_average.index, hourly_average.values, marker="o")

plt.title("Average Hourly Bicycle Counts on Fremont Bridge (2016)")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Total Bicycle Count")

plt.xticks(range(24))
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the plot in the same directory as hw1.py.
plt.savefig(script_directory / "counts_by_hour.png", dpi=300)

print("\nPlot saved as counts_by_hour.png")

plt.show()


# 10. Determine the busiest hour

busiest_hour = hourly_average.idxmax()
highest_average = hourly_average.max()

print("\nBusiest hour:", busiest_hour)
print("Average bicycle count:", round(highest_average, 2))

# Busiest hour of the day: 17


