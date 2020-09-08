'''pip 工具命令:
1- pip install <package_name> 下载第三方包
2- pip unistall <package_name> 删除第三方包
3- pip list 列出当前环境安装了那些模块和版本号
4- pip freeze 列出当前环境安装了那些模块和版本号
5- pip freeze > file_name 将列出的模块重定向(>)到指定文件里
6- pip install -r file_name 读取文件里的模块和版本号并安装

# 临时修改， 只修改这一个文件的下载路径
# 有多个可选服务器
7- pip install <package_name> -i <URL> 换下载服务器, 从指定路径下载第三方包

# 修改默认路径,即永久修改需要在当前用户的目录下创建一个pip文件夹,在新建一个文件pip.ini
# 往pip.ini里添加:
    [global]
    index-url = <你选的URL下载路径>
    [install]
    trusted-host = pypi.douban.com (如果选择了douban作为下载服务器)
'''
