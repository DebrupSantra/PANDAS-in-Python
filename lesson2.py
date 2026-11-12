import pandas as pd
marks=[85, 90, 78, 92, 88]
students=pd.Series(marks, index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print(students)
print(students.iloc[1]) 
print(students.loc['Charlie'])