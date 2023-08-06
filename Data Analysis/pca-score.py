import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from scipy.stats import linregress

df = pd.read_excel("transformed_data.xlsx", sheet_name = 0, index_col=0)

age_sheet = pd.read_excel("acel13073-sup-0002-tables1-s3.xlsx", sheet_name=1, header=[0,1])

ages = age_sheet.iloc[:, 3].values
df = df.T.values

# print(ages[0])
# print(df[0])

pca = PCA()
pca_scores = pca.fit_transform(df)

num_pcs = pca_scores.shape[1]

# Calculate p-values for each PC
p_values = []

for i in range(num_pcs):
    slope, intercept, r_value, p_value, std_err = linregress(ages, pca_scores[:, i])
    p_values.append(p_value)

# Convert to numpy array for easy indexing later
p_values = np.array(p_values)
top_2_pcs = p_values.argsort()[:2]  # Gets the indices of the two smallest p-values

print(top_2_pcs)