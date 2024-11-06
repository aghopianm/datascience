math_row = data[data[''] == 'Mathematics'].index[0]

# Extract the Mathematics values for Year 1 and Year 2
year1_math = data.iloc[math_row + 2, 0:4].astype(int).sum()
year2_math = data.iloc[math_row + 2, 4:8].astype(int).sum()

# Compare the values and print the result
if year1_math > year2_math:
    print("Year 1 Mathematics score is greater than Year 2.")
else:
    print("Year 2 Mathematics score is greater than or equal to Year 1.")