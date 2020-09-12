from bs4 import BeautifulSoup
import sqlite3
import urllib.request
import re
import xlwt


def main():

    baseUrl = "https://www.douban.com/doulist/4541413/?start=0"

    datalist_movie = getData(baseUrl)
    datalist_comment = getComment(baseUrl)

    savePath = "./国产良心剧/chinese_movie.xls"
    saveData(savePath, datalist_movie, datalist_comment)


find_link = re.compile(r'<a href="(.*?)" target="_blank">')
find_img = re.compile(r'<img src="(.*?)" width="100"/>', re.S)
find_title = re.compile(
    r'<a href.*target="_blank">(.*?)</a>', re.S
)
find_rating = re.compile(r'<span class="rating_nums">(.*)</span>')
find_judge = re.compile(r'<span>(.*)</span>')
find_main = re.compile(r'<div class="abstract">(.*?)</div>', re.S)
find_comment = re.compile(r'<span>评语：</span>(.*)</blockquote>', re.S)


def getData(baseUrl):  # 提取和解析网页信息
    datalist_movie = []
    for item in range(0, 7):
        url = baseUrl+str(item*25)
        html = askData(url)
        soup = BeautifulSoup(html, "html.parser")

        for i in soup.find_all("div", class_="bd doulist-subject"):  # 电影信息
            data = []
            item = str(i)  # 将影片信息转化成字符串

            link = re.findall(find_link, item)[0]
            data.append(link)

            img_link = re.findall(find_img, item)[0]
            data.append(img_link)

            title = re.findall(find_title, item)[0]
            data.append(title.strip())

            rating = re.findall(find_rating, item)[0]
            data.append(rating)

            judge = re.findall(find_judge, item)[0]
            data.append(judge)

            main = re.findall(find_main, item)[0]
            main = re.sub("<br(.*)?>(.*)?", "", main)
            main = re.sub("\n", "", main)
            main = re.sub('/', ',', main)
            data.append(main.strip())

            datalist_movie.append(data)

    return datalist_movie


def getComment(baseUrl):
    datalist_comment = []
    for item in range(0, 7):
        url = baseUrl+str(item*25)
        html = askData(url)
        soup = BeautifulSoup(html, "html.parser")
        for k in soup.find_all("div", class_="comment-item content"):  # 电影评语
            data = []
            item = str(k)

            comment = re.findall(find_comment, item)[0]
            comment = re.sub("\n", "", comment)
            data.append(comment.strip())

            datalist_comment.append(data)

    return datalist_comment


def askData(url):  # 请求网页信息
    # 编写头部信息
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")

    except Exception as e:
        if hasattr(e, "code"):
            print(e.code)

        if hasattr(e, "reason"):
            print(e.reason)

    return html


def saveData(savePath, datalist_movie, datalist_comment):  # 存储倒exel表格
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("国产电影推荐", cell_overwrite_ok=True)
    colums = ["超链接", "图片链接", "电影名", "评分", "评论人数", "主要人员", "评语"]
    for i in range(len(colums)):  # 列表名
        sheet.write(0, i, colums[i])

    for i in range(0, len(datalist_movie)):  # 电影信息
        data = datalist_movie[i]
        for k in range(0, len(data)):
            sheet.write(i+1, k, data[k])

    for i in range(0, len(datalist_comment)):  # 评语
        data = datalist_comment[i]
        for k in range(0, len(data)):
            sheet.write(i+1, 7, data[k])

    book.save(savePath)
    print("end...")


main()
