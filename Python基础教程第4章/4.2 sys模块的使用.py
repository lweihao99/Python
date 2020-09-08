# sys 模块
# 系统相关的模块
import sys


sys.exit(100)  # 终止程序等同于 exit(),默认结束码是0
print(sys.path)  # 结果是列表，表示查找模块的路径,只要模块实在这些路径的文件夹里，就可以导入
sys.stdin  # 可以像input一样， 接收用户的输入，和 input 相关
sys.stdout  # 标准输出,修改sys.stdout 可以改变默认输出位置
sys.stderr  # 修改sys.stderr 可以改变错误输出的默认位置,sys.stderr 和 sys.stdout默认都是在控制台
