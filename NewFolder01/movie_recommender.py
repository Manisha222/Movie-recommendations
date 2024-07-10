import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load movies data
movies = pd.read_csv('https://raw.githubusercontent.com/codeheroku/Introduction-to-Machine-Learning/master/Building%20a%20Movie%20Recommendation%20Engine/movie_dataset.csv')

# Select features for recommendation
features = ['keywords', 'cast', 'genres', 'director']

# Fill NaN values with empty string
for feature in features:
    movies[feature] = movies[feature].fillna('')

# Function to combine the selected features into a single string
def combine_features(row):
    return row['keywords'] + ' ' + row['cast'] + ' ' + row['genres'] + ' ' + row['director']

# Apply function to create a new 'combined_features' column
movies['combined_features'] = movies.apply(combine_features, axis=1)

# Create a count matrix from the combined features column
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies['combined_features'])

# Compute cosine similarity based on the count matrix
cosine_sim = cosine_similarity(count_matrix)

# Function to get movie recommendations based on title
def get_recommendations(title, cosine_sim):
    # Get index of the movie that matches the title
    idx = movies[movies['title'].str.lower() == title.lower()].index[0]

    # Get pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 10 recommendations (excluding the movie itself)
    sim_scores = sim_scores[1:11]

    # Get movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return top 10 most similar movies
    return movies['title'].iloc[movie_indices]

# Example usage
recommended_movies = get_recommendations('The Dark Knight Rises', cosine_sim)
print(recommended_movies)

