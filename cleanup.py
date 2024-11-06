import pandas as pd
import numpy as np

# Read the original dataset (if needed) into a DataFrame
x = pd.read_csv("CollegeGrades1.csv")  # Reading the original data into x

# If you need to create new DataFrames (like x or data2) from scratch, do that here
# Create the first DataFrame (x) if you want to overwrite it with new values
x = pd.DataFrame(np.nan,
                 index=['Year 1', 'Year 2', 'Evening'],
                 columns=[['Art', 'Engineering', 'Psychology', 'Mathematics', 'Technology', 'Chemistry'],
                          ['F P M D', 'F P M D', 'F P M D', 'F P M D', 'F P M D', 'F P M D']])

# Create the second DataFrame (data2)
data2 = pd.DataFrame(np.nan,
                     index=['M', 'F'],
                     columns=pd.MultiIndex.from_tuples([
                         ('Whitby', 'F P M D'),
                         ('Bridlington', 'F P M D'),
                         ('Scarborough', 'F P M D')
                     ]))

# Specify the path for the CSV file (this will overwrite the original)
file_path = "CollegeGrades1.csv"

# Write the first table (x) with title "a.)" and overwrite the original file
with open(file_path, 'w') as f:
    f.write("a.)\n")  # Title for the first table
    x.to_csv(f, index=True)  # Write the first DataFrame (x) to the file

# Append the second table (data2) with title "b.)"
with open(file_path, 'a') as f:
    f.write("\n\nb.)\n")  # Title for the second table with an extra blank line for separation
    data2.to_csv(f, index=True)  # Append the second DataFrame (data2) to the file