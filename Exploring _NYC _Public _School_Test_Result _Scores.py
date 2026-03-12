import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
print(schools.head())

best_math = schools[schools['average_math'] >= 0.8 * 800].sort_values(by='average_math', ascending=False)
best_math_schools= best_math[['school_name','average_math']]
print(best_math_schools)

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['total_SAT', 'school_name']].sort_values(by='total_SAT', ascending=False).head(10)
print(top_10_schools)


boroughs = schools.groupby('borough')['total_SAT'].agg(['count','mean', 'std']).round(2)
print(boroughs)


# Filter for max std and make borough a column
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Optional: Move borough from index to column
largest_std_dev.reset_index(inplace=True)

print(largest_std_dev)