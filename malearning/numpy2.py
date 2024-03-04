from fractions import Fraction
import numpy as np

# 设置矩阵元素输出用分数表示
np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

a = np.array([[1, 0, 0], [0, 1, 1], [0, 0, 1]])
print("分数形式显示原矩阵：")
print(a)

b = np.linalg.inv(a)  # 求逆矩阵
print("分数形式显示逆矩阵：")
print(b)
print("是否为E")
print(np.dot(b, a))
