import os
import os.path

i = 1
a = range(1, 2000)
name_list = list(a)
lst_files = os.walk('D:\\迅雷下载\\qdm传奇.2160p')

for dirpath, dirname, filename in lst_files:
    for file in filename:
        name = str(file)[:2] + '.mp4'
        src = os.path.join(dirpath, file)
        # 修改之后的目录加文件名
        dst = os.path.join(dirpath, name)
        os.rename(src, dst)
