import pandas as pd

# Příklad DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Skupinování a agregace dat
grouped = df.groupby('A').sum()
print(grouped)










