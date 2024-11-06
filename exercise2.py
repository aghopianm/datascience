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

# Set the second row (index 1) as the header
data.columns = data.iloc[1]  # Use the second row as the column headers
data = data.drop([0, 1])  # Drop the first two rows since they are now used as headers

# Check if subject names are now part of the columns
# print(data.columns)

# Find the column that contains 'Mathematics'
mathematics_columns = [col for col in data.columns if 'Mathematics' in str(col)]

if mathematics_columns:
    mathematics_column = mathematics_columns[0]  # Get the first occurrence of 'Mathematics'
else:
    print("Mathematics column not found.")
    exit()

# Now find the rows corresponding to "Year 1" and "Year 2"
year_1_row = data[data.iloc[:, 0] == 'Year 1']
year_2_row = data[data.iloc[:, 0] == 'Year 2']

# Extract the values under Mathematics for both Year 1 and Year 2
year_1_mathematics_values = year_1_row[mathematics_column].apply(pd.to_numeric, errors='coerce').sum()
year_2_mathematics_values = year_2_row[mathematics_column].apply(pd.to_numeric, errors='coerce').sum()

# Convert the results to scalar values (since they may be wrapped in a pandas Series)
year_1_total = year_1_mathematics_values.values[0] if isinstance(year_1_mathematics_values, pd.Series) else year_1_mathematics_values
year_2_total = year_2_mathematics_values.values[0] if isinstance(year_2_mathematics_values, pd.Series) else year_2_mathematics_values

# Compare the values
if year_1_total > year_2_total:
    print(f"Year 1 has a higher sum of Mathematics values: {year_1_total} > {year_2_total}")
else:
    print(f"Year 2 has a higher sum of Mathematics values: {year_2_total} > {year_1_total}")