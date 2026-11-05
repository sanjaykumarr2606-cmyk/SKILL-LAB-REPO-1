import pandas as pd

s = pd.Series(['apple', 'banana', 'mango', 'orange', 'grapes'])

print("Original Series:")
print(s)

print("Uppercase:")
print(s.str.upper())