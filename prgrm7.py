#7. Merging DataFrames Create two Pandas DataFrames with a common column. Merge the DataFrames using the common column.

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Ram', 'Sam', 'Raj']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Marks': [80, 90, 85]
})

result = pd.merge(df1, df2, on='ID')

print(result)
