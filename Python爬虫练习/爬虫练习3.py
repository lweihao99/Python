import re
from bs4 import BeautifulSoup
import urllib.request
import sqlite3
import xlwt



def main(): # 主程序

    print("Start")
    baseUrl = "https://movie.douban.com/top250?start=0"
    datalist = getData(baseUrl)
    savePath = r".\test.xls"


# 定义全局变量
findLink = re.compile(r'<a href="(.*?)">') # 链接
findImg = re.compile(r'<img .*src="(.*?)"',re.S) # 图片链接
findTitle = re.compile(r'<span class="title">(.*?)</span>') # 片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') #评分
findJudge = re.compile(r'<span>(\d*)人评价</span>') # 评分人数
findInq = re.compile(r'<span class="inq">(.*?)</span>') # 评语
findBd = re.compile(r'<p class="">(.*?)</p>',re.S) # 主要人员, 为什么找不到?


def getData(baseUrl): # 网页解析
    datalist = [] # 解析出来的数据存储对象

    for k in range(0,1):

        url = baseUrl+str(k*25)
        html = askUrl(url)
        soup = BeautifulSoup(html,"html.parser") # 解析使用 html.parser解析器解析html
        
        for i in soup.find_all("div",class_="item"): # 循环 class = "item"+ div 属性里的数据

            data = [] # 存储提取出来的数据
            i = str(i) # 字符串转化

            link = re.findall(findLink,i)[0] # 影片链接
            data.append(link)

            imgSrc = re.findall(findImg,i)[0] # 图片链接
            data.append(imgSrc)

            Title = re.findall(findTitle,i) # 影片片名
            if len(Title) == 2: # 可能有多个语言的片名,2个就是中文名和其他语言
                chTitle = Title[0]
                data.append(chTitle) # 中文名
                otTitle = Title[1]
                data.append(otTitle) # 其他语言片名
            else:
                data.append(Title[0])
                data.append(" ") # 留空，防止行数错乱


            Rating = re.findall(findRating,i)[0] # 评分
            data.append(Rating)

            Judge = re.findall(findJudge,i)[0] # 评分人数
            data.append(Judge)

            Inq = re.findall(findInq,i) # 评语
            if len(Inq)!=0: # 如果有评语
                Inq = re.sub("。",".",Inq[0])
                data.append(Inq)
            else:
                data.append(" ")

            Bd = re.findall(findBd,i) # 主要人员名
            Bd = str(Bd) 
            Bd = re.sub('<br(\s+)?/>(\s+)?'," ",Bd) # 去掉 <br/>
            Bd = re.sub("/"," ",Bd)
            data.append(Bd.strip()) # 去掉空格

            datalist.append(data)

    print(datalist)
    return datalist

def askUrl(url): # 获取网页信息

    head = { # 头部信息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    request = urllib.request.Request(url, headers=head) # 封装对象
    html = "" # 储存对象

    # 异常处理
    try:
        response = urllib.request.urlopen(request) # 请求对象
        html = response.read().decode("utf-8") # 读取数据
        
    except Exception as e:
        if hasattr(e,"code"): # 判断服务器可能出现的异常
            print(e.code)
        if hasattr(e,"reason"): # 判断没有捕获的原因
            print(e.reason)

    return html



if __name__=="__main__":

    main ()