#9. Create a Pandas DataFrame with MultiIndex consisting of 'Category' and 'SubCategory'. Fill the DataFrame with random data and compute the sum of values for each 'Category' and 'SubCategory'.

import pandas as pd
import numpy as np

index = pd.MultiIndex.from_arrays([
    ['A', 'A', 'B', 'B', 'C', 'C'],
    ['X', 'Y', 'X', 'Y', 'X', 'Y']
], names=['Category', 'SubCategory'])

df = pd.DataFrame({
    'Value': np.random.randint(1, 100, 6)
}, index=index)

print("DataFrame:")
print(df)

print("Sum of Values:")
print(df.groupby(level=['Category', 'SubCategory']).sum())
