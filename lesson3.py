import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [18, 19, 18, 20, 19],
    'Marks': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print(df)