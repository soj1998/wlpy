#### 每日记录

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



