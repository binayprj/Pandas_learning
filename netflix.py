# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
# Filter movies released between 1990 and 1999
netflix = netflix_df[netflix_df["type"] == "Movie"]
movies = netflix[(netflix['release_year'] >= 1990) & (netflix['release_year'] < 2000)]

plt.hist(movies['duration'])
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.title('Distribution of Movie Durations (1990-1999)')
plt.show()
duration = 100
action = movies[(movies["genre"]=="Action")]

short_movie_count=0
for label , row in action.iterrows():
    if row['duration'] < 90:
        short_movie_count += 1

print(short_movie_count)
    