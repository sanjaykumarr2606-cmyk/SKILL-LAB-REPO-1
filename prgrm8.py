#8. MultiIndex DataFrame Create a Pandas DataFrame with a MultiIndex (hierarchical index). Perform some basic indexing and slicing operations on the MultiIndex DataFrame.

import pandas as pd

index = pd.MultiIndex.from_tuples([
    ('A', 1), ('A', 2),
    ('B', 1), ('B', 2)
], names=['Category', 'Number'])

df = pd.DataFrame({
    'Value': [10, 20, 30, 40]
}, index=index)

print("DataFrame:")
print(df)

print("Single Row:")
print(df.loc[('A', 1)])

print("Category A:")
print(df.loc['A'])

print("Slicing:")
print(df.loc[('A', 1):('B', 1)])
