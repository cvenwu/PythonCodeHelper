# PythonCodeHelper
一些Python零碎代码 方便日后使用

1. astype()#数据类型转换 data['gender'] = (data['gender'] == 'male').astype(int)
2. pd.read_csv(fname,index_col=0)#把第一列当做索引
3. data['Embarked'].unique().tolist()#unique所有重复的值只留一个，tolist把矩阵或数组转化成列表
4. data['Embarked'].apply(lambda n:labels.index(n))#对每个元素使用apply函数  index检测n是在labels的第几个元素
> major_list = data['major'].unique().tolist()
> data['major'] = data['major'].apply((lambda x : major_list.index(x)))

5. train['Survived'].values#train['Survived']是DataFrame，要取其values才能传入训练模型使用
6. print('{0},{1}'.format(X.shape,y.shape))#format用{}和：代替%。{0}代表位置
7. a.append(b)#把b的指针放在a里面，b变了，a的内容也变了。

