from flask import Flask,render_template
import sqlite3
import jinja2

app = Flask(__name__) # 初始化

@app.route('/') # 网页路径
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/score')
def score():
    datalist = []
    legend = 'Top100视频'

    # 链接数据库
    con = sqlite3.connect(r'.\bilibili Top 100\哔哩哔哩Top100.db')
    cur = con.cursor()
    # 选择留言次数，和视频标题，和观看人数，比较观看人数和留言次数比例
    sql = "select comments,title,views,score,count(title) from bilibili_Top100 group by title" 
    data = cur.execute(sql)
    for item in data: # 进行数据追加
        datalist.append(item)

    cur.close
    con.close

    return render_template('score.html',data = datalist)
@app.route('/top100')
def videos():
    datalist = []
    # 链接数据库，进行数据查询
    con = sqlite3.connect(r'.\bilibili Top 100\哔哩哔哩Top100.db')
    cur = con.cursor()
    sql = "select * from bilibili_Top100" # 对目标数据库进行查询
    data = cur.execute(sql) # 将查询的数据赋值给data
    for item in data: # 遍历数据库数据
        datalist.append(item)
    cur.close()
    con.close()
    return render_template('Top100.html',videos = datalist) # 数据返回到网页上

@app.route('/word')
def wordCl():
    return render_template('word.html')


if __name__ == '__main__':

    app.run()