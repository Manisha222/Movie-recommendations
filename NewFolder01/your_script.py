import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from catboost import CatBoostRegressor

# Sample data creation for demonstration
data = {
    'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feature2': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'SalePrice': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
}
df = pd.DataFrame(data)

# Splitting the data into train and validation sets
X = df[['feature1', 'feature2']]
Y = df['SalePrice']
X_train, X_valid, Y_train, Y_valid = train_test_split(X, Y, test_size=0.2, random_state=42)

# Model training and prediction
cb_model = CatBoostRegressor(silent=True)
cb_model.fit(X_train, Y_train)

preds = cb_model.predict(X_valid)

# Calculating r2_score
cb_r2_score = r2_score(Y_valid, preds)
print(cb_r2_score)
