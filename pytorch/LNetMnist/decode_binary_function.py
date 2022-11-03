'''
解码二进制文件的函数
用来解码MNIST数据集里面的二进制文件

'''
import struct#struct模块
import numpy as np #numpy包


def decode_idx3_ubyte(idx3_ubyte_file):
    """
    解析idx3文件的通用函数
    :param idx3_ubyte_file: idx3文件路径
    :return: 数据集
    """
    # 读取二进制数据
    with open(idx3_ubyte_file, 'rb') as bin_data1:
        bin_data=bin_data1.read()
        # 解析文件头信息，依次为魔数、图片数量、每张图片高、每张图片宽
        offset = 0
        fmt_header = '>4i'
        '''使用大端法'''
        #mnist使用的大端方法存储的数据
        # 因为数据结构中前4行的数据类型都是32位整型，所以采用i格式，但我们需要读取前4行数据，所以需要4个i。我们后面会看到标签集中，只使用2个ii。
        magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
        print('魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols))

        # 解析数据集
        image_size = num_rows * num_cols
        # 获得数据在缓存中的指针位置，从前面介绍的数据结构可以看出，读取了前4行之后，指针位置（即偏移位置offset）指向0016。
        print(struct.calcsize(">4i"))
        offset =offset+ struct.calcsize(fmt_header)
        print(offset)
        # 图像数据像素值的类型为unsigned char型，对应的format格式为B。这里还有加上图像大小784，是为了读取784个B格式数据，如果没有则只会读取一个值（即一副图像中的一个像素值）
        #B是一个字节8为，I是4个字节32位
        fmt_image = '>' + str(image_size) + 'B'
        print(fmt_image,offset,struct.calcsize(fmt_image))
        #1万张图片
        images = np.empty((num_images, num_rows, num_cols))
        #plt.figure()
        #j=0
        for i in range(num_images):
            if (i + 1) % 10000 == 0:
                print('已解析 %d' % (i + 1) + '张')
                print(offset)
            #读取数据放入第i行，并reshape（28，28）
            images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
            #print("输出",images[i])
            offset += struct.calcsize(fmt_image)
            #plt.imshow(images[i],'gray')
            #不明白是什么意思

            #plt.pause(0.001)
            #plt.show()
        #plt.show()

        return images


def decode_idx1_ubyte(idx1_ubyte_file):
    """
    解析idx1文件的通用函数
    :param idx1_ubyte_file: idx1文件路径
    :return: 数据集
    """
    # 读取二进制数据
    with open(idx1_ubyte_file, 'rb') as bin_data1:
        bin_data=bin_data1.read()
        # 解析文件头信息，依次为魔数、图片数量、每张图片高、每张图片宽
        offset = 0
        fmt_header = '>2i'
        '''使用大端法'''
        #mnist使用的大端方法存储的数据
        # 因为数据结构中前4行的数据类型都是32位整型，所以采用i格式，但我们需要读取前4行数据，所以需要4个i。我们后面会看到标签集中，只使用2个ii。
        magic_number, num_labels = struct.unpack_from(fmt_header, bin_data, offset)
        print('魔数:%d, 图片标签数量: %d个' % (magic_number, num_labels))

        # 解析数据集
        label_size = 1
        # 获得数据在缓存中的指针位置，从前面介绍的数据结构可以看出，读取了前4行之后，指针位置（即偏移位置offset）指向0016。
        print(struct.calcsize(">2i"))
        offset =offset+ struct.calcsize(fmt_header)
        print(offset)
        # 图像数据像素值的类型为unsigned char型，对应的format格式为B。这里还有加上图像大小784，是为了读取784个B格式数据，如果没有则只会读取一个值（即一副图像中的一个像素值）
        #B是一个字节8为，I是4个字节32位
        fmt_label = '>' + str(label_size) + 'B'
        print(fmt_label,offset,struct.calcsize(fmt_label))
        #1万张图片
        labels = np.empty((num_labels, 1))
        #plt.figure()
        j=0
        for i in range(num_labels):
            labels[i] = np.array(struct.unpack_from(fmt_label, bin_data, offset)).reshape(1)
            #print("输出",images[i])
            offset += struct.calcsize(fmt_label)
            #plt.imshow(images[i],'gray')
            #不明白是什么意思

            #plt.pause(0.001)
            #plt.show()
        #plt.show()

        return labels
