from matplotlib import pyplot as plt
import pandas as pd
from scipy import stats
from scipy.stats import zscore
import numpy as np
import seaborn as sns

# Replace 'filename.xlsx' with your file path
df = pd.read_excel('transformed_data.xlsx', sheet_name = 0, index_col=0)  # assuming patient IDs are the first column

# print(df)

# print(df_normalized)

class_sheet = pd.read_excel('acel13073-sup-0002-tables1-s3.xlsx', sheet_name = 0, header=[0])

# print(class_sheet.iloc[:,11])

for i in range(0, len(df.index.values)):
    df.index.values[i] = class_sheet.iloc[:,11][i] 

df.index = df.index.fillna('unknown compounds')
# Strip whitespace from the index values
df.index = df.index.str.strip()

df['row_median'] = df.median(axis=1)

# Sort the DataFrame first by index and then by the row_median
df_sorted = df.sort_values(by=['row_median'], kind='mergesort').sort_index(kind='mergesort').drop('row_median', axis=1)

print(df_sorted)

# print(df_normalized.index.values[769])

# for i in range(0, len(df_normalized.index.values)):
#     df_normalized.index.values[i] = class_sheet[i][10]

# df_collabed.to_excel('intricated_data.xlsx')

plt.figure()
sns.heatmap(df_sorted, cmap='coolwarm', cbar_kws={'label': 'Intensity'})

# Adjustments for better visualization
plt.title('Heatmap of Metabolites vs. Patients')
plt.xticks(rotation=45, ha='right')  # Rotate column labels for better visibility
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()