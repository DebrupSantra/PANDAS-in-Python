import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [18, 19, 18, 20, 19],
    'Marks': [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)
print(df[['Name', 'Marks']])
print(df.head(3))
print(df[df['Marks'] > 85])
print(df.tail(2))
print(df[df['Name'] == 'Charlie'])