import pandas as pd
data = pd.read_csv('./1.csv')
# 获取数据的行数和列数
print(data.shape[0], data.shape[1])
