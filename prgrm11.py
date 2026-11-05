import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (6, 3)),
                  columns=['A', 'B', 'C'])

df['Total'] = df.apply(lambda x: x['A'] + x['B'] + x['C'], axis=1)

print(df)