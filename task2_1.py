import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Netflix dataset
netflix_data = pd.read_csv('netflix_data.csv')

# Display the first few rows to understand the data
print(netflix_data.head())

# Visualization 1: Distribution of 'type' (TV Show or Movie)
plt.figure(figsize=(6, 4))
sns.countplot(x='type', data=netflix_data, palette='Set2')
plt.title('Distribution of TV Shows and Movies')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# Visualization 2: Top 10 countries with the most content available on Netflix
top_countries = netflix_data['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='muted')
plt.title('Top 10 Countries with the Most Content on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()
# release year distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=netflix_data, x='release_year', bins=30, kde=True, color='skyblue')
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()
#rating distribution

plt.figure(figsize=(8, 5))
sns.countplot(x='rating', data=netflix_data, order=netflix_data['rating'].value_counts().index, palette='pastel')
plt.title('Distribution of Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


#duration distribution
movies_data = netflix_data[netflix_data['type'] == 'Movie']
plt.figure(figsize=(10, 6))
sns.histplot(data=movies_data, x='duration', bins=30, kde=True, color='salmon')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.show()
