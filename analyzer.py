import pandas as pd

# 读取CSV
df = pd.read_csv('students.csv')

# 先看看数据长什么样
print(df)
print("\n总行数:", len(df))