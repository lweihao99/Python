# 常见的内置模块
# 1. OS 模块 (OperatingSystem)
# os 模块里提供的方法就是用来调用操作系统里的方法

import os

# os.name --> 获取操作系统的名字 windows 系列 ==> nt / 非 windows 系统==> posix
print(os.name)  # nt
print(os.sep)  # 路径的分隔符 windows \ ， 非 windows /


# os 模块里的 path 方法
print(os.path.abspath('4.0导入函数的五种方式.py'))  # abspath 获取文件的绝对路径
os.path.isdir("venv")  # True --> isdir 判断是否是文件夹, 所以要是文件就会返回 False
# os.path.isfile()  # isfile 判断是否是一个文件, 返回True or False
# os.path.exists()  # exists 判断是否存在， 返回True or False


file_name = '2020.2.21.demo.py'
# print(file_name.rpartition('.'))  # 获得('2020.2.21.demo', '.', 'py'),分隔文件名和它的后缀
# 也能获得('2020.2.21.demo', '.py') 功能类似于 rpartition()
print(os.path.splitext(file_name))


# os 里的其他方法

os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录
os.chdir("test")  # 改变当前脚本工作目录，相当于shell下的cd命令
os.rename("1.txt", "2.txt")  # 文件重命名
os.remove("1.txt")  # 删除文件
os.rmdir("demo")  # 删除空文件夹
os.removedirs('demo')  # 删除空文件夹
os.mkdir('demo')  # 创建一个文件夹
os.chdir('../')  # 切换工作目录,(../) 是返回到上一目录
os.listdir('c:\\')  # 列出指定目录里的所有文件和文件夹
os.environ  # 获取到环境配置
os.environ.get('PATH')  # 获取到指定的环境配置
