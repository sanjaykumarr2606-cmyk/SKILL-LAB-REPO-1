#12. Working with Text Data Create a Pandas Series with 5 random text strings. Convert all the strings to uppercase.

import pandas as pd

s = pd.Series(['apple', 'banana', 'mango', 'orange', 'grapes'])

print("Original Series:")
print(s)

print("Uppercase:")
print(s.str.upper())
