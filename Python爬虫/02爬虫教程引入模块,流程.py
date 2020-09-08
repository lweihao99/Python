
from bs4 import BeautifulSoup # 网页解析
import re  # 正则表达式,进行文字匹配
import urllib.request  # 制定URL,获取网页数据
import xlwt  # 进行exel操作
import sqlite3  # 进行SQlite数据库操作
"""
构建流程
1、爬取网页
2、解析数据
3、保存数据

"""

# 主要程序流程
def main():  
    print("开始爬取")
    # 1、爬取网页
    baseUrl = "https://movie.douban.com/top250?start=0"
    # 调用getData函数,datalist返回值返回到这里,函数嵌套看3.1
    datalist = getData(baseUrl)
    
    # 定义保存路径savepath
    # savepath = r".\豆瓣电影TOP250.xls"  # ./  是当前文件夹
    # 调用保存数据
    # saveData(datalist,savepath)

    # dbpath = "movie.db" # 保存数据库目录
    # saveData2Db(datalist,dbpath) # 函数调用



# 定义一个全局变量

findLink = re.compile(r'<a href="(.*?)">') # 创建一个正则表达式对象，一个规则,字符串模式, 看 05正则表达式内容补充 # 影片详情链接的规则

findImg = re.compile(r'<img.*src="(.*?)"',re.S) # 影片图片信息, re.S 让换行符包含在字符中

findTitle = re.compile(r'<span class="title">(.*)</span>') # 影片片名

findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') # 影片评分

findJudge = re.compile(r'<span>(\d*)人评价</span>') # 找到评价人数, \d是数字

findInq = re.compile(r'<span class="inq">(.*)</span>') # 找到概况

findBd = re.compile(r'<p class="">(.*?)</p>',re.S) # 找到影片的相关内容, 导演和演员



# 解析网页
def getData(baseUrl):  
    # 定义datalist
    datalist = []

    for i in range(0,10): # 调用获取页面获取信息的函数， 10次， 每次25条信息--->i*25
        url = baseUrl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码
        
        # 2、逐一解析网页数据，没获取一个网页就分析网页数据
        soup = BeautifulSoup(html,"html.parser") # 解析html这个对象
        #对文档进行提取
        for item in soup.find_all("div",class_="item"):  # 查找符合要求的字符串,形成列表, 查找所有 class= "item"+ div 的信息
            # print(item) # 测试: 查看电影item全部信息
            
            data = [] # 保存一部电影的全部信息
            item = str(item) # 转化成字符串，方便比较, 用正则表达式对字符串进行判断和解析

            # 获取影片详情的链接
            link = re.findall(findLink,item)[0] # re 库用来查找指定字符串, 规定模式, 如果能找到匹配的字符串那么第一个[0]元素就我们想要的链接
            data.append(link) # 添加链接
            
            imgSrc = re.findall(findImg,item)[0] 
            data.append(imgSrc) # 添加图片
            
            titles = re.findall(findTitle,item) # 片名可能只有一个中文名没有外国名, 或者中文外文都有, 所以没有限制下标索引
            if (len(titles)==2): # 判断有几个片名， 如果有两个就说明有中文名和外国名
                ctitle = titles[0] 
                data.append(ctitle) # 存储中文片名
                otitle = titles[1].replace("/","") # 将无关符号 "/" 去掉(替换成 "")
                data.append(otitle) # 添加外国名
            else:
                data.append(titles[0])
                data.append(" ") # 外国名留空, 防止错乱

            rating = re.findall(findRating,item)[0]
            data.append(rating) # 添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum) # 添加评价人数

            Inq = re.findall(findInq,item)
            if len(Inq)!= 0: # 如果长度 != 0 就是有内容
                Inq = Inq[0].replace("。","") # 替换 。 
                data.append(Inq) # 添加概述
            else:
                data.append("") # 没有概述的话，留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) # 去掉<br/> 
            bd = re.sub("/"," ",bd) # 去掉 /
            data.append(bd.strip()) # .strip 去掉前后空格

            datalist.append(data) # 把处理好的一部电影信息放入 datalist 列表
            break
    print(datalist)
    return datalist

# 得到指定一个URL的网页内容

def askURL(url): # 调用一个页面信息的函数
    # 写入user agent信息,在网页源码里找
    head = {
        #在发送请求的时候伪装成浏览器,(本质上是告诉浏览器我们可以接收什么水平的内容)
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    #发送消息
    request = urllib.request.Request(url,headers = head) # 将我们的头部信息封装给head,然后携带者头部信息来访问URL, 用 urllib.request 这个对象来访问
    html = "" #存储
    try:
        response = urllib.request.urlopen(request) #  封装好的信息发送请求并返回response对象 (response 是表示能够接收回封装信息的对象)，所以这个response 对象就有我们整个网页的信息
        html = response.read().decode("utf-8") # 读取response 的网页信息
        # print(html)
        
    except urllib.error.URLerror as e: # 有可能会出现的异常
        if hasattr(e,"code"): # 判断访问这个服务器之后有什么问题
            print(e.code)
        # has attribute 指的是标签
        if hasattr(e,"reason"): # 查看是什么原因他没有捕获成功
            print(e.reason)

    return html


def saveData(datalist,savepath):  # 保存数据
    print("save..")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建 workbook 对象, 可以理解为一个文件
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")

    for i in range(0,8):
        sheet.write(0,i,col[i]) # 列名

    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for k in range(0,8):
            sheet.write(i+1,k,data[k]) # 数据

    book.save(savepath)



def saveData2Db(datalist,dbpath): # 保存到数据库
    init_db(dbpath) # 调用函数
    conn = sqlite3.connect(dbpath) # 链接数据库
    cur = conn.cursor() # 游标
    

    for data in datalist: # 循环datalist 列表里的元素
        for index in range(len(data)): # 索引,范围是datalist 的所有元素(这里是250个)
            if index ==4 or index ==5: # 下表4,5是数值所以跳过 # 不用添加双引号
                continue

            data[index] ='"'+data[index]+'"' # 给值加上双引号
        
        sql = '''
            insert into movie250(
                info_link,pic_link,cname,ename,score,rated,introduction,info
            )
            values(%s)'''%",".join(data) # 将data列表用逗号链接起来

        
        # print(sql)
        cur.execute(sql)
        conn.commit()
    
    cur.close()
    conn.close()




def init_db(dbpath): # 创建数据库, 需要路径:dbpath
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    ''' # 创建数据表内容
    conn = sqlite3.connect(dbpath) # 链接或者创建数据库
    cursor = conn.cursor() # 游标,存放SQL语句执行结果
    cursor.execute(sql) # 执行SQL语句
    conn.commit() # 让数据库生效
    conn.close() # 关闭链接



if __name__ == "__main__": # 当程序执行时
    # 调用函数
    main()
    print("爬取完毕")