# 参考文章：https://www.jianshu.com/p/26a7dbc15246
import torch
import torch.nn as nn
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


x = [i for i in range(100)]
y = [i for i in range(100)]

model = Model()

LEARNING_RATE = 0.9
## 学习率等间隔衰减
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE, momentum=0.9)
# 学习率衰减()：每50epoch 设置为10%
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 5, 0.1)
# 到时需使用scheduler.step()

for epoch in range(10):
    print(optimizer.param_groups[0]['lr'])
    scheduler.step()
