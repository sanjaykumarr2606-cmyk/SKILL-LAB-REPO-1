import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Product': ['Pen', 'Book', 'Pencil', 'Bag', 'Scale'],
    'Category': ['A', 'B', 'A', 'C', 'B'],
    'Sales': np.random.randint(100, 1000, 5)
})

print(df)

result = df.groupby('Category')['Sales'].sum()

print("Total Sales:")
print(result)