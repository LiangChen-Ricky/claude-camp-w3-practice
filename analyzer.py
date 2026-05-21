import pandas as pd

# 读取CSV
df = pd.read_csv('students.csv')

# 先看看数据长什么样
print(df)
print("\n总行数:", len(df))
total = len(df)
print(df['country'].value_counts())
df['country'].value_counts().to_dict()
counts = df['bet_status'].value_counts().to_dict()
completed = counts['completed']
completion_rate = round(completed / total * 100, 1)

print(f"对赌完成率: {completion_rate}%")