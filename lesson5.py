
import pandas as pd

data = {
    'Employee': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Karan', 'Riya'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'Salary': [35000, 28000, 42000, 50000, 30000, 45000],
    'Experience': [2, 1, 4, 5, 2, 4]
}

df = pd.DataFrame(data)

print(df[['Employee', 'Salary']])

print(df.head(4))

print(df[df['Salary'] > 35000])


print(df[df['Department'] == 'IT'])


print(df.tail(3))

print(df[df['Experience'] >= 4])
