import numpy as np
import pandas as pd

# Load the data from the CSV files
x = pd.DataFrame(pd.read_csv("Grades1.csv"))
y = pd.DataFrame(pd.read_csv("Grades2.csv"))

# Merge the dataframes as before
data = pd.merge(x, y, how='outer', left_index=True, right_index=True)

# Rename all columns that contain "Unnamed" to an empty string
data.columns = ["" if "Unnamed" in str(col) else col for col in data.columns]

# Save the cleaned DataFrame to a new CSV file
data.to_csv("Cleaned2.csv", index=False)

# Drop unwanted rows
data = data.drop(0, axis=0)
data = data.drop(2, axis=0)
data = data.drop(3, axis=0)
data = data.drop(4, axis=0)
data.to_csv("test.csv", index=False)

# Load the data with multi-level headers
data = pd.read_csv("test2.csv", header=[0, 1])  # Using the first two rows as headers for location and subject

# Function to process numerical data and sum the next 3 values
# Dictionary to store results
results = {}

# Loop through locations to find "Mathematics"
for location in data.columns.levels[0]:  # Iterate through each unique location
    if "Mathematics" in data[location].columns:  # Check if "Mathematics" exists under this location
        print(f"Processing Mathematics data for location: {location}")

        # Extract "Mathematics" data for the current location
        math_data = data[location]["Mathematics"].dropna().reset_index(drop=True)

        # Check if math_data has enough rows to support our indexing logic
        if len(math_data) < 4:
            print(f"Not enough data for Mathematics in location {location}")
            continue

        # Initialize variables for each group
        year1_m_sum = 0
        year1_f_sum = 0
        year2_m_sum = 0
        year2_f_sum = 0

        # Year 1 Male (Row 0) - Sum the first cell and the next 3 cells across the row
        year1_m_sum = math_data.iloc[0:1].values[0:4].sum()  # Sum across Year 1 Male

        # Year 1 Female (Row 1)
        year1_f_sum = math_data.iloc[1:2].values[0:4].sum()  # Sum across Year 1 Female

        # Year 2 Male (Row 2)
        year2_m_sum = math_data.iloc[2:3].values[0:4].sum()  # Sum across Year 2 Male

        # Year 2 Female (Row 3)
        year2_f_sum = math_data.iloc[3:4].values[0:4].sum()  # Sum across Year 2 Female

        # Store results for this location
        results[location] = {
            "Year 1 - M": year1_m_sum,
            "Year 2 - M": year2_m_sum,
            "Year 1 - F": year1_f_sum,
            "Year 2 - F": year2_f_sum,
        }

        # Comparison outputs
        if year1_m_sum > year2_m_sum:
            print(f"{location} - Male: Year 1 has a higher score than Year 2 ({year1_m_sum} > {year2_m_sum})")
        else:
            print(f"{location} - Male: Year 2 has a higher score than Year 1 ({year2_m_sum} > {year1_m_sum})")

        if year1_f_sum > year2_f_sum:
            print(f"{location} - Female: Year 1 has a higher score than Year 2 ({year1_f_sum} > {year2_f_sum})")
        else:
            print(f"{location} - Female: Year 2 has a higher score than Year 1 ({year2_f_sum} > {year1_f_sum})")

# Summary of all locations
print("\nSummary of results for all locations:")
for loc, res in results.items():
    print(f"{loc}: {res}")
