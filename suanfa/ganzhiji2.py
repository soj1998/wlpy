from numpy import *
import matplotlib.pyplot as plt
import operator
import time


def createTrainDataSet():  # 训练样本,第一个1为阈值对应的w，下同
    trainData = [[1, 1, 4],
                 [1, 2, 3],
                 [1, -2, 3],
                 [1, -2, 2],
                 [1, 0, 1],
                 [1, 1, 2]]
    label = [1, 1, 1, -1, -1, -1]
    return trainData, label


def createTestDataSet():  # 数据样本
    testData = [[1, 1, 1],
                [1, 2, 0],
                [1, 2, 4],
                [1, 1, 3]]
    return testData


def sigmoid(X):
    X = float(X)
    if X > 0:
        return 1
    elif X < 0:
        return -1
    else:
        return 0


def pla(traindataIn, trainlabelIn):
    traindata = mat(traindataIn)  # 将列表转换成矩阵http://www.cnblogs.com/itdyb/p/5773404.html
    trainlabel = mat(trainlabelIn).transpose()  # 矩阵的转置中
    m, n = shape(traindata)
    w = ones((n, 1))  # ones函数是用于生成一个全1的数组,eye函数用户生成指定行数的单位矩阵,.T作用于矩阵，用作球矩阵的转置
    while True:
        iscompleted = True
        for i in range(m):
            if (sigmoid(dot(traindata[i], w)) == trainlabel[
                i]):  # 同线性代数中矩阵乘法的定义： np.dot(),http://blog.csdn.net/u012609509/article/details/70230204
                continue
            else:
                iscompleted = False
                w += (trainlabel[i] * traindata[i]).transpose()
        if iscompleted:
            break
    return w


def classify(inX, w):
    result = sigmoid(dot(mat(inX), w))
    if result > 0:
        return 1
    else:
        return -1


def plotBestFit(w):
    traindata, label = createTrainDataSet()
    dataArr = array(traindata)
    n = shape(dataArr)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []
    for i in range(n):
        if int(label[i]) == 1:
            xcord1.append(
                dataArr[i, 1])  # 关于array: line 52，http://www.zmonster.me/2016/03/09/numpy-slicing-and-indexing.html
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 这些是编码为单个整数的子图栅格参数。例如，”111″表示“1×1网格，第一子图”，”234″表示“2×3网格，第4子图”。
    # https://gxnotes.com/article/19844.html
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-w[0] - w[1] * x) / w[2]
    ax.plot(x, y)
    plt.xlabel('X1');
    plt.ylabel('X2')
    plt.show()


def classifyall(datatest, w):
    predict = []
    for data in datatest:
        result = classify(data, w)
        predict.append(result)
    return predict


def main():
    trainData, label = createTrainDataSet()
    testdata = createTestDataSet()
    w = pla(trainData, label)
    result = classifyall(testdata, w)
    plotBestFit(w)
    print(w)
    print(result)


if __name__ == '__main__':
    start = time.process_time()
    main()
    end = time.process_time()
    print('finish all in %s' % str(end - start))
