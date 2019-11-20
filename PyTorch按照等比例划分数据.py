'''
运行结果：
train: 60000, test: 10000
train: 50000, val: 10000, test: 10000
'''

import torch
from torchvision import datasets, transforms
transform = transforms.Compose([
                                transforms.ToTensor()
                                ])

data_dir = '../../Lesson7/自己写/data/MNIST'


train_MNIST_data = datasets.MNIST(root=data_dir, train=True, download=False, transform=transform)
test_MNIST_data = datasets.MNIST(root=data_dir, train=False, download=False, transform=transform)
# 将train_dataset划分为train_dataset与valid_dataset
print('train: {}, test: {}'.format(len(train_MNIST_data), len(test_MNIST_data)))  # 60000, 10000
train_MNIST_data, val_MNIST_data = torch.utils.data.random_split(train_MNIST_data, [50000, 10000])
print('train: {}, val: {}, test: {}'.format(len(train_MNIST_data), len(val_MNIST_data), len(test_MNIST_data)))
