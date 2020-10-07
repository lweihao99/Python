import urllib.request
import sqlite3
from bs4 import BeautifulSoup
import re
import xlwt

def main(): # 主程序

    baseUrl = 'https://www.bilibili.com/ranking' # 目标网站网址

    datalist = getData(baseUrl) # 调用数据分析函数，返回值赋值给datalist,给参数赋值

    # savePath = r'.\bilibili Top 100\bilibili Top100.xls' # exel表格存储目录
    # 调用保存数据函数
    # saveData(savePath,datalist)

    dbpath = r'.\bilibili Top 100\哔哩哔哩Top100.db' # 数据库路径
    saveData2db(datalist,dbpath) # 数据库函数调用


findlink = re.compile(r'<a class="title" href="(.*?)" target="_blank">') # 视频超链接
findtitle = re.compile(r'<img alt="(.*?)" src=""/>') # 视频标题
findUp = re.compile(r'<i class="b-icon author"></i>(.*?)</span>') # 作者
findviews = re.compile(r'<i class="b-icon play"></i>(.*?)</span>') # 播放次数
findcomment = re.compile(r'<i class="b-icon view"></i>(.*?)</span>') # 留言数
findpts = re.compile(r'<div>(\d*)</div>') # 综合得分



def getData(baseUrl):

    datalist = [] # 保存所有视频信息总列表
    url = baseUrl
    html = askUrl(url) # html 返回值
    soup = BeautifulSoup(html,'html.parser') # 解析html信息对象
    # 逐一解析获取到的数据
    for item in soup.find_all("div",class_="content"):
        # print(item)
        # break
        data = [] # 存储一部视频信息
        item = str(item) # 将信息转化成字符串

        # 开始提取数据
        link = re.findall(findlink,item)[0]
        data.append(link)

        title = re.findall(findtitle,item)[0]
        data.append(title)

        author = re.findall(findUp,item)[0]
        data.append(author)

        views = re.findall(findviews,item)[0]
        data.append(views)

        comments = re.findall(findcomment,item)[0]
        data.append(comments)

        pts = re.findall(findpts,item)[0]
        data.append(pts)

        datalist.append(data)
        # break
    # print(datalist)
    return datalist




def askUrl(url): # 获取网页信息

    # 编写头部信息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head) # 封装信息给request对象
    html = "" # 存储对象
    # 异常处理
    try:
        response = urllib.request.urlopen(request) # 请求对象
        html = response.read().decode('UTF-8') # 读取请求对象信息

    except Exception as e:
        
        if hasattr(e,'code'): # 判断访问服务器出错原因
            print(e.code)
        if hasattr(e,'reason'): # 判断没有捕获到数据的原因
            print(e.reason)
    
    return html




def saveData(savePath,datalist): # 保存数据到表格

    print("开始保存..")
    book = xlwt.Workbook(encoding="UTF-8",style_compression=0) # 创建exel文件
    sheet = book.add_sheet("哔哩哔哩Top100",cell_overwrite_ok=True) # 在文件里创建表格单
    colums = ('视频超链接','视频标题','视频作者','视频观看数','视频留言数','视频综合得分') # 定义列表名

    for i in range(0,6):
        sheet.write(0,i,colums[i]) # 列名

    for i in range(0,len(datalist)):
        print("第%d条"%(i+1))
        data = datalist[i]
        for k in range(0,len(data)):
            sheet.write(i+1,k,data[k]) # 列出数据
    
    book.save(savePath)



def init_db(dbpath): # 创建数据库

    sql ='''
        create table bilibili_top100
        (
        id integer primary key autoincrement,
        info_link text,
        title varchar,
        author varchar,
        views varchar,
        comments varchar,
        score numeric
        )
    
    '''# 创建数据列表
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()




def saveData2db(datalist,dbpath):

    init_db(dbpath)
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    # 索引数据，插入到数据库里
    for data in datalist:
        for index in range(len(data)):
            if index == 5:
                continue
            data[index] = '"'+data[index]+'"'

        sql= '''
            insert into bilibili_Top100(
                info_link,title,author,views,comments,score
            )
            values(%s)'''%",".join(data)

        # print(sql)
        cur.execute(sql)
        con.commit()
    cur.close()
    con.close()








if __name__=='__main__':

    main()