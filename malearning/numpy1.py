from fractions import Fraction
import numpy as np

# 设置矩阵元素输出用分数表示
np.set_printoptions(formatter={'all': lambda x: str(Fraction(x).limit_denominator())})

a = np.array([[1, -1, 0], [0, 1, -1], [-1, 0, 1]])
e = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print("分数形式显示原矩阵：")
print(a)

b = np.linalg.inv(a-2*e)  # 求逆矩阵
print("分数形式显示逆矩阵：")
print(b)

print("矩阵X：")
c = np.dot(b, a)
print(c)

print("两边相等-左边")
d = np.dot(a, c)
print(d)

e = 2*c
print("两边相等-右边")
print(2*c + a)

print("重新开始")
a1 = np.array([[0, 1, -1], [-1, 0, 1], [1, -1, 0]])
print(np.dot(a, a1))
print(2*a1 + a)


