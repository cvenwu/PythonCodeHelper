
# 使用visdom同时画两条线
import numpy as np

import visdom
vis = visdom.Visdom()


Y = np.linspace(-5, 5, 100)
vis.line(
         Y=np.column_stack((Y * Y, np.sqrt(Y + 5))), #函数参数是一个元祖
         X=np.column_stack((Y, Y)),
         opts=dict(markers=False, showlegend=True),
         )
