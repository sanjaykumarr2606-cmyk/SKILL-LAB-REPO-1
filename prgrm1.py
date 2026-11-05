import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (5, 3)),
                  columns=['A', 'B', 'C'])

df['Product'] = df['A'] * df['B']

print(df)
