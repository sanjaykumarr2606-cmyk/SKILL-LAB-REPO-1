#Create a Pandas DataFrame with 2 columns: 'Category' and 'Value'. Fill the 'Category' column with random categories ('A', 'B', 'C') and the 'Value' column with random integers. Group the DataFrame by 'Category' and compute the sum and mean of 'Value' for each category.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], 10),
    'Value': np.random.randint(1, 100, 10)
})

print("DataFrame:")
print(df)

result = df.groupby('Category')['Value'].agg(['sum', 'mean'])

print("Aggregation:")
print(result)
