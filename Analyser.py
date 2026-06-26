import pandas as pd

data = pd.read_csv('attacks.csv')

print("First 10 attacks:")
print(data.head(10))

print("\nColumns:")
print(data.columns.tolist())

print("\nTotal attacks: " + str(len(data)))

print("\nUnique attacker IPs: " + str(data['ip'].nunique()))
print("\nTop attacking IPs:")
print(data['ip'].value_counts().head(10))