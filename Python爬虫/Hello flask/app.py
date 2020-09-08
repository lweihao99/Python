from flask import Flask,render_template,request # render_template 渲染模板,文件必须在templates文件夹下, 
# request是请求，将用户端的表单信息封装好了传给我们
import jinja2
import datetime

app = Flask(__name__) # 使用默认全局变量'__name__',初始化对象 app, 将自身的框架导入到程序里



@app.route('/') # 路由解析,通过用户访问的路径，匹配相应的函数
# 匹配的是下面的函数, 标记了如果用户访问的是 '/' 就return字符串
def hello_world():
    return "你好" # 如果没有开启 debug 模式(默认是关闭的), 是不会时时的上传到服务器更新内容

@app.route('/index')
def index():
    return "Hello,ciao"


@app.route("/user/<name>") # 通过用户访问路径，获取用户的字符串参数
def welcome(name): # 将用户输入到<name> 的值传到函数里赋值给参数,从而使name显示用户输入的值

    return "你好,%s"%name

@app.route("/user/<int:id>") # 传用户输入的id 到函数里, 整形参数, 还可以有float 类型
def welcome2(id):

    return "Hello,%d"%id+"Master"

# 路由的路径不能重复, 用户通过唯一路径访问特定的函数
# 返回给用户渲染后的网页文件
# @app.route("/h")
# def index2():
    
#     return render_template("index.html") # 执行index.html 文件,

# 向页面传递一个变量

@app.route("/h")
def index3():
    
    time = datetime.date.today() # 普通变量, 网页渲染用的
    name = ['嚣张','小张','小赵'] # 列表类型
    task = {"任务":"打扫卫生","时间":"3小时"} # 字典类型
    return render_template("index.html", var = time, list = name, task = task) # 变量存储

# 表单提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")

@app.route('/result',methods=['POST','GET']) # 创建一个提交之后的结果页面,
# 接受表单提交的路由，需要指定methods 为POST 要不然会显示method not allowed,默认是使用get
def result():
    if request.method == 'POST':
        result = request.form # form 将表单里的信息形成了一个字典, key 是 name ='姓名'的'姓名',输入的值就是 value
        return render_template("test/result.html",result=result)

if __name__ == "__main__":

    app.run() # 启动服务器, 启动调试模式(debug 模式)---> 不是在所有开发环境都有效