# 网页信息爬取加标签提取练习
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib

# 定义主程序函数
def main():
    print("开始爬取")
    # 定义目标网址
    baseUrl = "https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3"
    # 调用getData 函数赋值给 datalist
    datalist = getData(baseUrl)
    # 定义保存路径
    savePath = r".\bilibili top100.xls"


# 进行全局变量声明
# 创建一个正则表达式规则，查找信息时的规则
findLink = re.compile(r'<a href="(.*?)"target="_blank>') # 视频链接
findImg = re.compile(r'<img alt="(.*?)"src="(.*?)">') # 图片信息
findTitle = re.compile(r'class="title">(.*)</a>') # 标题
findViews = re.compile(r'<i class="b-icon play"></i>"(.*?)"</span>') # 观看次数
findComment = re.compile(r'<i class="b-icon view"></i>"(.*?)"</span>') # 留言人数
findAuthor = re.compile(r'<i class="b-icon author"></i>"(.*?)"</span>') # 作者
findPts = re.compile(r'<div>\d</div>"(.*?)</div>"') # 综合分数


# 网页分析
def getData(baseUrl):
    # 定义一个存储信息的空列表
    datalist = []
    
    for i in range(0,1):
        # 提取有用信息
        url = baseUrl # 将网址赋值给 url 参数
        # 保存获取到的网页源码
        html = askUrl(url)
        # 逐一分析网页信息，并解析网页数据
        soup = BeautifulSoup(html,"html.parser") # 使用html.parser 解析器
        # 逐一查找符合要求的字符串
        for item in soup.find_all("div",class_="content"):
                
            data = [] # 保存每一次提取出来的全部信息
            item = str(item) # 将数据转化成字符串,方便比较

            link = re.findall(findLink,item) #查找匹配字符串
            data.append(link) # 添加链接

            Img = re.findall(findImg,item) # 查找图片信息
            data.append(Img) # 添加图片信息

            title = re.findall(findTitle,item) # 查找标题
            data.append(title) # 添加标题

            views = re.findall(findViews,item) # 查找观看次数
            data.append(views) # 添加观看次数

            comments = re.findall(findComment,item) # 查找留言人数
            data.append(comments)

            author = re.findall(findAuthor,item) # 查找作者名
            data.append(author)

            points = re.findall(findPts,item) # 查找综合得分
            data.append(points)

            datalist.append(data) # 将一部处理好得信息发送给 datalist 列表
            
            # print(item)
    print(datalist)

    return datalist




# 网页爬取
def askUrl(url):
    # 封装头部信息
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    # 从新模拟浏览器，封装浏览器信息给 request 对象
    request = urllib.request.Request(url, headers = head)
    html = ""  # 存储对象

    # 异常抓取
    try:
        # 声明一个请求对象
        response = urllib.request.urlopen(request)
        # 读取对象
        html = response.read().decode("utf-8")

    except urllib.error.URLerror as e:  # 判断可能出现的异常
        if hasattr(e, "code"):  # 判断服务器可能出现问题
            print(e.code)

        if hasattr(e, "reason"):  # 判断没有捕获成功的原因
            print(e.reason)
    # 返回读取了的数据
    return html


if __name__ == "__main__":  # main 入口

    main()
