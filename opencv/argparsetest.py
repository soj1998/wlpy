import argparse

# (1) 声明一个parser
parser = argparse.ArgumentParser()

# (2) 添加参数
parser.add_argument("parg")  # 位置参数，这里表示第一个出现的参数赋值给parg
parser.add_argument("--digit", type=int, help="输入数字")  # 通过 --echo xxx声明的参数，为int类型
parser.add_argument("--name", help="名字", default="cjf")  # 同上，default 表示默认值

# (3) 读取命令行参数
args = parser.parse_args()

# (4) 调用这些参数
print(args.parg)
print("echo ={0}".format(args.digit))
print("name = {}".format(args.name))

# 命令行测试 python opencv/argparsetest.py position_arg --digit 2222

