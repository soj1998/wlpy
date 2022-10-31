### 每日记录

### 2022年9月29日

>1. 创建环境
    使用conda prompt conda create envname python=3.8  
    conda activate envname  
    在pycharm中设置interpreter 选exists 选择环境的python.exe  
    在conda prompt中 pip3 install  
    win32api、win32gui、win32con、Pillow、numpy、opencv、PyQt5 
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python  
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-contrib-python    
    pip3 install -i https://pypi.doubanio.com/simple PyQt5 
    安装PIL pip3 install -i https://pypi.doubanio.com/simple  pillow 
>2. pywin32在windows环境下需要设置环境变量  
    首先用pip3 show pywin32命令查看包安装的位置  
    要找到pywin32_system32，注意不是包位置，设置到环境变量  
    重启pycharm 仍然报错 但可用  
    安装pywin32 pip3 install -i https://pypi.doubanio.com/simple pywin32 
>3. pyhook3也需要环境变量  
    一、下载swig并解压官方链接： http://www.swig.org/download.html  
    二、复制swig文件夹的根目录添路径，添加到环境变量。
       右击“此电脑”——属性——系统高级设置——环境变量——选择“path”，点击“编辑”——新建——粘贴路径。  
    三、安装visualstudio2017：链接：https://visualstudio.microsoft.com/zh-hans/downloads/  
       进入界面后选择：下载——最下方折叠框打开——  
       点击“用于VisualStudio2017的工具”的下载——双击安装——勾选
       “VisualC++生成工具”，
       同一界面复选框中勾选“适用于桌面的VisualC++2015.3V14.0工具集”
       ——安装——结束  
       第三步应该不用，注意swig下载windows版本
    四、重新cmd——pip install pyHook3安装就不会报错。   
    五、python3版本如果已经使用pyhook模块，把import pyHook改为 import PyHook3 as pyHook就能正常运行了
    pip3 install -i https://pypi.doubanio.com/simple PyHook3
>4. 安装pyautogui  
   pip3 install -i https://pypi.doubanio.com/simple pyautogui  
>5. 安装matplotlib  
   pip3 install -i https://pypi.doubanio.com/simple matplotlib  
>6. 安装md转html的包  
   pip3 install -i https://pypi.doubanio.com/simple markdown  
   pip3 install -i https://pypi.doubanio.com/simple importlib  
>7. 安装pytorch  
   pip3 install torch==1.8.2 torchvision==0.9.2 torchaudio===0.8.2 --extra-index-url 
   https://download.pytorch.org/whl/lts/1.8/cpu  
>8. 出现错误The given NumPy array is not writeable, and PyTorch does not support non-writ  
   /data/home/file_name/.conda/envs/cmr/lib/python3.7/site-packages/torch/utils/data/_utils/collate.py:63  
  将 return default_collate([torch.as_tensor(b) for b in batch])
  修改为 return default_collate([torch.as_tensor(b.copy()) for b in batch])
>9. pyqt5截图出现pil支持pyqt6   
  pip3 install -i https://pypi.doubanio.com/simple PyQt6  
>10. 不要安装argparse  
  pip3 install -i https://pypi.doubanio.com/simple argparse    
  这个是个标准库 要在外面运行py文件
>11. 安装imutils  
  imutils是Adrian Rosebrock开发的一个python工具包，它整合了opencv、numpy和matplotlib的相关操作，主要是用来进行图形图像的处理，如图像的平移、旋转、缩放、骨架提取、显示等等，后期又加入了针对视频的处理，如摄像头、本地文件等。imutils同时支持python2和python3。  
  pip3 install -i https://pypi.doubanio.com/simple imutils    
