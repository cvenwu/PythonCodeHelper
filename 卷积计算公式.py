# 卷积计算层次大小公式
import math

def CalcConv(w, h, f, p, s):
    """
    :param w: 输入的图片宽度
    :param h: 输入的图片高度
    :param f: 卷积核大小
    :param p: padding的值
    :param s: stride的值
    :return:
    """
    w = math.floor((w-f+2*p) / s + 1)
    h = math.floor((h-f+2*p) / s + 1)
    return w, h


# print(calc(100, 30, 3, 4, 1))
# print(calc(53, 18, 3, 0, 2))
# print(calc(13, 8, 3, 1, 1))

print(CalcConv(100, 30, 3, 1, 1))
