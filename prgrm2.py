#2. Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers. Compute the row-wise and column-wise sum.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (4, 3)),
                  columns=['A', 'B', 'C'])

print("DataFrame:")
print(df)

print("Row-wise Sum:")
print(df.sum(axis=1))

print("Column-wise Sum:")
print(df.sum(axis=0))
