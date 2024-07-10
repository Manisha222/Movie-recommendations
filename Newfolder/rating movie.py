import pandas as pd
from sklearn.model_selection import train_test_split

# Replace 'ratings.csv' with the correct path to your dataset
ratings_data = pd.read_csv('C:/Users/dell/Desktop/New folder/New folder/ratings.csv')

# Data preprocessing
ratings_data.dropna(inplace=True)  # Drop rows with missing values
train_data, test_data = train_test_split(ratings_data, test_size=0.2)

# Continue with your feature engineering, model selection, training, and evaluation steps.
