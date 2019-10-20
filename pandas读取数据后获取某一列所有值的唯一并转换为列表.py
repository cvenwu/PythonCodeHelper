# pandas读取数据以后，获取某一列的值的唯一表示

import pandas as pd
data = pd.read_csv('./1.csv')

# 例如获取gender列的所有数据，并筛选出唯一值然后转换为列表
column_ele_list = data['gender'].unique().tolist()

