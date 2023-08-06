import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# Generate some sample data
# X would be your dataset with age, metabolites etc. and y would be your continuous response variable

df = pd.read_excel('acel13073-sup-0002-tables1-s3.xlsx', sheet_name=2)

# transposed_df = df.T

# transposed_df.to_excel('transposed_patients.xlsx', index=True)

with_age_df = pd.read_excel('transposed_patients.xlsx', sheet_name = 0)

with_age_df = with_age_df.drop(0)
with_age_df = with_age_df.to_numpy()
print(with_age_df.shape)
# with_age_df = np.delete(with_age_df, 0, axis = 1)

# print(with_age_df)

X = with_age_df[:,1:-1]
y = with_age_df[:,-1]

print(X.shape, y.shape)

# X, y = np.random.rand(1000, 30), np.random.rand(1000,)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Standardize the data
scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Define the hyperparameters and their possible values
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

# Initialize RandomForest
rf = RandomForestRegressor()

# Grid search with 5-fold cross-validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Get the best model
best_rf = grid_search.best_estimator_

feature_importances = best_rf.feature_importances_
sorted_indices = np.argsort(feature_importances)[::-1]
for index in sorted_indices:
    print(f"Feature {X.columns[index]}: {feature_importances[index]}")

# Predict on test set
y_pred = best_rf.predict(X_test)

# Evaluate performance
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")