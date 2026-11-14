
import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Webcam'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'Price': [55000, 800, 1500, 12000, 2500, 3000],
    'Stock': [10, 50, 30, 15, 8, 25]
}

df = pd.DataFrame(data)

print(df[['Product', 'Price']])

print(df.head(3))

print(df[df['Price'] > 2000])

print(df[df['Category'] == 'Accessories'])

print(df.tail(2))

print(df[df['Stock'] < 15])

print(df[(df['Price'] > 1000) & (df['Stock'] > 10)])
