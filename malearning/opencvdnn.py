# 导入工具包 学习文章 https://zhuanlan.zhihu.com/p/88745033 OpenCv的DNN模块学习记录
# 百度搜索 opencv cv2.dnn_readNetFromCaffe lenet_iter_10000.caffemodel
import numpy as np
import cv2

# 标签文件处理
rows = open("label.txt").read().strip().split("\n")
classes = [r[r.find(" ") + 1:].split(",")[0] for r in rows]

# Caffe所需配置文件
# 读取模型，一个网络模型文件，一个参数文件
modelTxt = 'classificat_net.prototxt'
modelBin = 'lenet_iter_10000.caffemodel'
net = cv2.dnn.readNetFromCaffe(modelTxt,
	modelBin)

# 图像路径
imagePaths = 'moban.jpg'

# 图像数据预处理
image = cv2.imread(imagePaths)
#temp = cv2.cvtColor(np.asarray(image), cv2.COLOR_RGB2BGR)
#ref = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
#image = cv2.threshold(ref, 100, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('abc', image)
cv2.waitKey()
cv2.destroyAllWindows()
resized = cv2.resize(image, (28, 28))
# 拿到了第一张啤酒的图片resized

# image scalefactor size mean swapRB
# cv2.dnn.blobFromImage 用于对输入网络的图像进行预处理，主要是三部分，1.减均值 2.缩放 3.通道变换(可选)，对于imageNet训练集而言，三通道均值为(104, 117, 123)
blob = cv2.dnn.blobFromImage(resized, 1, (28, 28), (104, 117, 123))
# caffe 输出四维的数据 batchsize channel h w
print("First Blob: {}".format(blob.shape))

# 得到预测结果
net.setInput(blob)
preds = net.forward()
# print(preds) preds相当于一个数组，就是我们将图片input网络后，网络吐出了一个记录了1000多个种类得分的数组

# 排序，取分类可能性最大的
idx = np.argsort(preds[0])[::-1][0]
text = "Label: {}, {:.2f}%".format(classes[idx],
	preds[0][idx] * 100)

# 将文本信息添加到图片上，参数分别是，图片，文本，呈现位置，字体，大小，颜色，颜色厚度
cv2.putText(image, text, (5, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (255, 255, 0), 2)

# 显示
cv2.imshow("Image", image)
cv2.waitKey(0)


