import pandas as pd

# 打印名字
print("我的名字：张泽乾")

# pandas读取csv
df = pd.read_csv("data.csv")
print("\n读取到的csv数据：")
print(df)