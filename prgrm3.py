import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (5, 3)),
                  columns=['A', 'B', 'C'])

df.iloc[1, 0] = np.nan
df.iloc[3, 1] = np.nan

print("Before filling:")
print(df)

df = df.fillna(df.mean())

print("After filling:")
print(df)