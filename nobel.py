# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
nobel= pd.read_csv('nobel.csv')
#What is the most commonly awarded gender and birth country?
top_gender= nobel['sex'].value_counts().index[0]
print("\n The gender with the most Nobel laureates is :", top_gender)
top_country= nobel['birth_country'].value_counts().index[0]
print(" The most common birth country of Nobel laureates is :", top_country)

#Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
nobel['United States of America']= nobel['birth_country']=='United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['United States of America'].mean()
max_decade_usa = prop_usa_winners[prop_usa_winners['United States of America'] == prop_usa_winners['United States of America'].max()]['decade'].values[0]
ax1 = sns.relplot(x='decade', y='United States of America', data=prop_usa_winners, kind="line")

#Which decade and Nobel Prize category combination had the highest proportion of female laureates?
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_decade_category = prop_female_winners[prop_female_winners['female_winner'] == prop_female_winners['female_winner'].max()][['decade', 'category']]
max_female_dict = {max_female_decade_category['decade'].values[0]: max_female_decade_category['category'].values[0]}
ax2 = sns.relplot(x='decade', y='female_winner', hue='category', data=prop_female_winners, kind="line")

# Finding the first woman to win a Nobel Prize
nobel_women = nobel[nobel['female_winner']]
min_row = nobel_women[nobel_women['year'] == nobel_women['year'].min()]
first_woman_name = min_row['full_name'].values[0]
first_woman_category = min_row['category'].values[0]
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Selecting the laureates that have received 2 or more prizes
counts = nobel['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)

print("\n The repeat winners are :", repeat_list)