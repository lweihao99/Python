from flask import Flask,render_template,request
import datetime # 导入实时时间模块

app = Flask(__name__) # 使用默认全局变量 __name__ , 初始化 app 对象,将Flask框架导入进来

@app.route('/',methods=["POST","GET"])
def submit():
    date = datetime.date.today()
    time = datetime.time.strftime()
    TVshow = ["Running man","闲着干吗呢","雾山五行"]
    duration = ["1个半小时","1小时25分钟","没看"]

    music = {"周杰伦":["七里香","稻香","画沙"],"Marshmello":["Friend","Here with me","Happier"],
            "邓紫棋":"光年之外","李玖哲":"夏天","Ed Sheeran":["Photograph","Galway girl","Perfect"]}
    
    return render_template("regist.html",var = date,time = time,tvshow = TVshow,duration = duration,music = music)

if __name__ == "__main__":

    app.run()

