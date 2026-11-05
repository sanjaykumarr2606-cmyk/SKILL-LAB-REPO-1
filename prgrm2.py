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