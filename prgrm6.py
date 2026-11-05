#6. Create a Pandas DataFrame with 3 columns: 'Product', 'Category', and 'Sales'. Fill the DataFrame with random data. Group the DataFrame by 'Category' and compute the total sales for each category.

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
