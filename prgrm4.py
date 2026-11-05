#4. Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers. Introduce some NaN values. Drop the rows with any NaN values

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (6, 4)),
                  columns=['A', 'B', 'C', 'D'])

df.iloc[1, 0] = np.nan
df.iloc[3, 2] = np.nan

print("Before dropping:")
print(df)

df = df.dropna()

print("After dropping:")
print(df)
