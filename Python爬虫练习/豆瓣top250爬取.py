# 豆瓣Top250 爬取
import re
from bs4 import BeautifulSoup
import urllib.request
import xlwt
import sqlite3

def main(): # 主程序

    baseUrl = "https://movie.douban.com/top250?start=0" # 目标网址

    # savePath = r"./豆瓣Top250个人版.xls"
    dataList = getData(baseUrl)

    # saveData(dataList,savePath) # 给saveData 参数定义

    dbpath = "豆瓣top250.db" # 定义一个数据库储存目录
    saveSqlData(dataList,dbpath) # 调用SQL函数



findLink = re.compile(r'<a href="(.*?)">') # 影片链接
findImg = re.compile(r'<img.*src="(.*?)"',re.S) # 图片链接
findTitle = re.compile(r'<span class="title">(.*)</span>') # 片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>') # 影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>') # 评价人数
findRecape = re.compile(r'<span class="inq">(.*)</span>') # 概括
findBd = re.compile(r'<p class="">(.*?)</p>',re.S) # 主要人员信息


def getData(baseUrl): # 逐一解析并提取网页数据

    dataList =[] # 数据总列表

    for item in range(0,10):

        url = baseUrl+str(item*25)
        html = askUrl(url) # 将html 返回值赋值给 html
        soup = BeautifulSoup(html,"html.parser") # 解析数据

        for i in soup.find_all("div",class_="item"):

            data = [] # 存储单部影片信息列表
            i = str(i) # 将数据转化成字符串

            # 开始爬取各种信息
            link = re.findall(findLink,i)[0]
            data.append(link) # 添加链接

            Img = re.findall(findImg,i)[0]
            data.append(Img) # 添加图片链接

            Title = re.findall(findTitle,i)
            if len(Title)==2:
                chTitle = Title[0] # 第一个影片片名是中文
                data.append(chTitle) # 添加中文片名

                otherTitle = Title[1] # 其他语言片名
                otherTitle = re.sub("/","",otherTitle)
                data.append(otherTitle) # 添加其他语言片名
            else:
                data.append(Title[0])
                data.append(" ") # 只有中文名

            Rating = re.findall(findRating,i)[0]
            data.append(Rating) # 添加评分

            JudgementPPl = re.findall(findJudge,i)[0]
            data.append(JudgementPPl) # 添加评价人数

            Recape = re.findall(findRecape,i)
            if len(Recape)!=0: # 判断有没有概括信息
                Recape = Recape[0].replace("。","") # 中文句号要去掉，不然会生成一个列表, recape会包含在一个列表里
                data.append(Recape) # 没有就留空
            else:
                data.append(" ") # 如果有概括信息就添加

            MainChar = re.findall(findBd,i)[0]
            MainChar = re.sub("<br(.+)?/>(\s+)?"," ",MainChar)
            MainChar = re.sub("/",",",MainChar)
            data.append(MainChar.strip()) # 添加主要人员信息

            dataList.append(data) # 将每部电影信息存储到总列表里

    return dataList




def askUrl(url): # 获取网页信息

    head = { # 伪装头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

    request = urllib.request.Request(url,headers=head) # 封装对象
    html = "" # 存储对象

    try:
        response = urllib.request.urlopen(request) # 请求对象
        html = response.read().decode("utf-8") # 储存解析出来的数据

        

    except Exception as e: # 判断可能出现的异常

        if hasattr(e,"code"): # 判断服务器异常
            print(e.code)

        if hasattr(e,"reason"): # 判断没有捕获异常的原因
            print(e.reason)

    return html


def saveData(dataList,savePath): # 数据保存

    book = xlwt.Workbook(encoding="utf-8",style_compression=0) # 创建xls文件
    sheet = book.add_sheet("豆瓣Top 250",cell_overwrite_ok=True) # 创建表格单
    colums = ("电影链接","电影图片链接","电影中文片名","电影外国片名","评分","评分人数","总结","主要人员名单")

    for i in range(0,8):
        sheet.write(0,i,colums[i]) # 添加列表名
    
    for i in range(0,250):
        print("第%d条"%(i+1)) # 查看保存到了第几条
        data = dataList[i]
        for k in range(0,8):
            sheet.write(i+1,k,data[k]) # 将 dataList 里的子列表里的8个元素分别保存到合适的位置

    book.save(savePath)

def saveSqlData(dataList,dbpath):

    init_db(dbpath) # 调用函数
    conn = sqlite3.connect(dbpath) # 从新连接已经生成了的数据库
    cur = conn.cursor() # 生成游标,存放数据库里的sql结果

    # 由于每一列的元素是单个元素，所以需要从dataList 里索引
    for data in dataList:
        for index in range(len(data)): # 索引dataList 里的 data 列表里的单一元素,范围是所有data列表也就是250个影片信息
            if index == 4 or index == 5: # 下标4，5是整数元素
                continue # 跳过循环


            data[index] = '"'+ data[index] + '"' # 给字符串元素添加双引号,因为...

        # 将data里的影片信息插入到数据表里
        sql ='''
            insert into movieTop250(
                info_link,pic_link,chName,otName,score,rating,recape,info
            )
            values(%s)
        '''%",".join(data) # 使用join来拼接列表，并且使用逗号区分开来
        # values()是给上面相对应的列表赋值
        # print(sql)
        cur.execute(sql) # 执行新的sql语句
        conn.commit() # 使数据库生效
    
    cur.close() # 关闭数据库
    conn.close()


def init_db(dbpath): # 创建数据表

    sql ='''
        create table movieTop250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        chName varchar,
        otName varchar,
        score numeric,
        rating numeric,
        recape text,
        info text
        )
    '''  # 创建数据表内容
    conn = sqlite3.connect(dbpath) # 连接数据库或者创建一个新的数据库
    cursor = conn.cursor() # 游标,存放SQL执行结果
    cursor.execute(sql)
    conn.commit() # 数据库生效
    conn.close() # 关闭数据库

if __name__ == "__main__": # 主程序入口

    main()

    print("save complete")