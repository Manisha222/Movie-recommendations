import pandas as pd

# Correct file paths
ratings_file_path = 'C:/Users/dell/Downloads/ml-100k/u.data'
movies_file_path = 'C:/Users/dell/Downloads/ml-100k/u.item'

# Load ratings data
column_names = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv(ratings_file_path, sep='\t', names=column_names)

# Load movies data
movies = pd.read_csv(movies_file_path, sep='|', encoding='latin-1', header=None,
                     names=['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL', 'unknown', 'Action', 'Adventure',
                            'Animation', 'Children', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 
                            'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'])

print(ratings.head())
print(movies.head())

