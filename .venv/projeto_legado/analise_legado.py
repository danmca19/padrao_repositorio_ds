import pandas as pd

print(f"Versão do Pandas: {pd.__version__}")

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.append({'A': 4, 'B': 7}, ignore_index=True)
print(df)
