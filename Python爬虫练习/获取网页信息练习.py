# 导入模块
import urllib.request # 导入 request 对象 # 指定URL 获取网页数据的模块
import xlwt
# 定义主函数

def main(): #主要程序流程
    
    print("开始爬取")

    #1、爬取网页-->获得基本地址
    baseUrl = "https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3"

    dataList = getData(baseUrl) # 调用 getData 函数, baseUrl 参数, 将返回的数据列表信息赋值给主程序 dataList

    savePath = r".\bilibili top list.xls" # 保存路径
    # 调用 askUrl 函数, 并给参数赋值
    askUrl("https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3")


# 获取网页数据并分析

def getData(baseurl):

    # 定义数据列表
    dataList = []


    return dataList # 返回数据列表到主程序

# 得到指定URL网页内容, 访问 URL
def askUrl(url):
    # 封装头部信息，模拟真实浏览器
    head = {
        # 封装 User-Agemt 信息, 模拟真实浏览器访问
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    # 将头部信息封装给一个访问对象
    request = urllib.request.Request(url, headers=head) # 要想加入 headers 信息,需用 Request 来构造请求,从新封装, 用 urlopen()发起请求
    html = "" # 存储对象
    #捕获异常
    try:
        # 将所有封装好的网页信息发给请求对象
        response = urllib.request.urlopen(request) # request 是封装好的对象, 将封装好的所有信息返回给 response 对象, 并发起请求
        html = response.read().decode("utf-8") # 读取网页信息 并储存, 读取 response 请求对象的信息并解码
        print(html) # 打印读取出来的网页信息
    
    # 判断可能出现的异常
    except Exception as e:
        if hasattr(e,"code"): # 判断访问了这个服务器可能出现的问题
            print(e.code)
        if hasattr(e,"reason"): # 判断没有捕获成功的原因
            print(e.reason)
    
    # 将读取并储存了的信息返回给主程序
    return html


if __name__ == "__main__": # 主程序入口

    main()
