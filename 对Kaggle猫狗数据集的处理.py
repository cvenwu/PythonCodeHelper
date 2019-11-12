
# kaggle中的猫狗数据集处理
# data_file_path 指定kaggle下载后数据集的train1目录
# data_path 指定数据要存储的目录

# 程序运行结果
# - data_process.py 就是本文件
# - data
#   - dogs-vs-cats kaggle下载的文件解压后的目录
#     - test1
#     - train
#   - train 将kaggle下载好的数据中train1移动到该目录
#     - dog 存放标签为dog的训练数据
#     - cat 存放标签为cat的训练数据
#   - test
#     - dog 存放标签为dog的测试数据
#     - cat 存放标签为cat的测试数据


import shutil
import os

data_path = './data/train'


data_file_path = './data/dogs-vs-cats/train'

def data_process(data_file_path):
    '''
        将原来的数据重新划分
        :param data_file_path: 原来数据存储的路径
        :return:
        '''
    data_file_list = os.listdir(data_file_path)
    for i in data_file_list:
        img_class = i.split('.')[0]
        img_name = i.split('.')[1]
        shutil.move(os.path.join(data_file_path, i), os.path.join(data_path+'/'+img_class+'/'+img_name+'.jpg'))

data_process(data_file_path)
