#13. Create a Pandas Series with 5 random text strings. Extract the first three characters of each string.

import pandas as pd

s = pd.Series(['apple', 'banana', 'mango', 'orange', 'grapes'])

print("Original Series:")
print(s)

print("First Three Characters:")
print(s.str[:3])
