import urllib.request  # request 对象

# *获取 get 请求
# 解析网页,通过 .utlopen 打开网页
# 将打开网页或得到的所有数据返回给变量名,比如 response
# response = urllib.request.urlopen("http://www.baidu.com")
# # .read 读取所有对象返回的信息; 为了避免乱码使用 .decode()用来解码,默认是 utf-8
# print(response.read().decode("utf-8"))  # .decode("utf-8") 将前面返回的信息用utf-8来解析


#* 获取 post 请求, 需要封装,模拟真实浏览器请求
# 用 httpbin.org 测试网站
import urllib.parse # .parse 解析器

# #使用解析器来解析一下，然后按照一定的格式，比如utf-8的格式，最后在使用bytes转化成二进制 ，在封装到数据包 data 里
# #urlencode 封装数据,里面是字典
# #在urlencode的括号外面还要说明二进制bytes 数组是按照什么方式封装的,比如用 utf-8 将字典里内容封装
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")  # 将信息转化成二进制的数据包 如 int将其他数据类型转化成整数
# # 想要访问post需要传递一个post的表单信息,然后通过表单信息的封装来访问post
# #data就是要传递给post的内容
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

# *get 超时处理
# 如果超时未响应,就进行异常处理
# 如果执行的过程中，超时未响应了，就跳过，去做其他事情
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)#timeout = n; 如果在n 秒以内没有响应就会报错
#     print(response.read().decode("utf-8"))
# except Exception as e:
#     print("timeout")

# 其他信息捕获
# response = urllib.request.urlopen("http://www.baidu.com",timeout=1)
# # print(response.status) # .status 状态码，如果是200就说明状态正常，404就是找不到了
# # print(response.getheaders()) # 获得网页的headers
# print(response.getheader("server")) # 获得网页的单个 header 信息



# *如何防止被识破是爬虫，如何伪装成浏览器
# url ="https://www.douban.com"
# 示例
# 请求的头部信息
# url = "http://httpbin.org/post"
# headers = {
#     # 字典
#     #   key           value
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
#     # 用这段信息伪装成浏览器,模拟浏览器，将信息封装起来
# }

# # 想要不被识破的话,需要把请求对象从新封装一下
# # 由于用的是 post 需要在封装一下
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST") # 请求对象, POST 要大写
# response = urllib.request.urlopen(req) # 由封装对象来传递信息
# print(response.read().decode("utf-8"))

url ="https://www.douban.com"
# 用户代理信息
headers = {
    # 字典
    #   key           value
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    # 用这段信息伪装成浏览器,模拟浏览器，将信息封装起来
}

req = urllib.request.Request(url=url,headers=headers) # 请求对象
response = urllib.request.urlopen(req) # 由封装对象来传递信息
print(response.read().decode("utf-8"))

u