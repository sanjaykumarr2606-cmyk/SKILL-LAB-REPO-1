import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (5, 3)),
                  columns=['A', 'B', 'C'])

print("Original DataFrame:")
print(df)

result = df.apply(lambda x: x * 2)

print("After Doubling:")
print(result)