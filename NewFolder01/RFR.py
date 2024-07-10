from sklearn.ensemble import RandomForestRegressor
 

model_RFR = RandomForestRegressor(n_estimators=10)
model_RFR.fit(X_train, Y_train)

Y_pred = model_RFR.predict(X_valid)
 
mean_absolute_percentage_error(Y_valid, Y_pred)