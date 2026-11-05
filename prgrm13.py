import pandas as pd

s = pd.Series(['apple', 'banana', 'mango', 'orange', 'grapes'])

print("Original Series:")
print(s)

print("First Three Characters:")
print(s.str[:3])