import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print(movies.head())
print(ratings.head())
avg_rating = ratings.groupby('movieId')['rating'].mean()
print(avg_rating.head())
rating_count = ratings.groupby('movieId')['rating'].count()
print(rating_count.head())
movie_data = pd.DataFrame({
    'avg_rating': avg_rating,
    'rating_count': rating_count
})

print(movie_data.head())
top_movies = movie_data.sort_values(by='avg_rating', ascending=False)
print(top_movies.head(10))
filtered_movies = movie_data[movie_data['rating_count'] > 50]

top_movies = filtered_movies.sort_values(by='avg_rating', ascending=False)

print(top_movies.head(10))

top_movies = top_movies.merge(movies, on='movieId')

print(top_movies[['title', 'avg_rating', 'rating_count']].head(10))
def recommend_by_genre(genre):
    filtered = movies[movies['genres'].str.contains(genre, case=False)]
    return filtered[['title', 'genres']].head(10)
print(recommend_by_genre("Action"))
def recommend_by_genre(genre):
    filtered = movies[movies['genres'].str.contains(genre, case=False)]
    result = filtered.merge(movie_data, on='movieId')
    return result.sort_values(by='avg_rating', ascending=False)[['title', 'avg_rating']].head(10)
print(recommend_by_genre("Action"))
import matplotlib.pyplot as plt

plt.hist(ratings['rating'])
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
top10 = top_movies.head(10)

plt.figure()
plt.barh(top10['title'], top10['avg_rating'])
plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.title("Top 10 Movies")
plt.show()