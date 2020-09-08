from bs4 import BeautifulSoup # 网页信息解析
# 将网页里需要的部分给提取出来

"""
BeautifulSoup 是将赋复杂的 HTML 文档转换成一个复杂的树形结构, 每个节点都是Python 对象, 所有对象可以归纳为4种:

1. Tag
2. NavigableString
3. BeatifulSoup
4. Comment
""" 
# 1. Tag
# 打开文件
file = open("./baidu.html","rb") # rb 二进制的读取,将文件读取到内存里, 模拟将网页爬取之后，获取到内存的数据文件

# 将 file 读到一个对象里
html = file.read()

# 解析 html 文档
bs = BeautifulSoup(html,"html.parse") # 要有一个对象,这里是 BeatifulSoup, 而这个对象需要指定一个解析器 () 
# 解析器就是需要一个对象， 比如 bs 来帮助我们来分析文档, 由于这里的文档是 html 类型的， 就用 html.parse 解析器

print(bs.title) # 将文档里的 title 标签,以及其所有内容提取出来

print(bs.title.string) # 如果只想要内容不要标签---> 类型是 NavigatableString

# 这就是 1.Tag 标签及其内容, 默认是拿第一个遇到的标签和内容


# 2.NavigatableString 标签里的内容(字符串)

print(bs.a.attrs) # attrs 可以拿到标签里的所有属性值,用字典的方式来保存


# 3.BeatifulSoup 表示整个文档

print(bs.name) # name 就是文档

print(bs.attrs) # 标签是空的

print(bs) # 打印整个文档, 类型就是 BeatifulSoup 本身, 把嵌套都去掉了


# 4. Comment

print(bs.a.string) # 没有包含注释的内容 ---> 类型是 Comment 是一个特殊的NavigatableString, 输出的内容不包含注释符号


# *------------------------------分割线-----------------------------------------------------

# 节点的获取
# 文档的遍历 ---> 将整个文档里的相似的东西全部找到
print(bs.head.contents) # contents 文档遍历的属性 --> 返回列表
print(bs.head.contents[1]) # 由于是列表所以可以用下标来访问


# 文档的搜索 ---> 精准定位想要的内容

# 1. find_all() 查找所有
# 字符串过滤: 会查找所有与字符串完全匹配的内容
t_list = bs.find_all("a") # 查询所有 a 标签, 统一放到列表里
print(t_list) # 返回列表 , 将 a 标签的所有内容给找出来

# 2.正则表达式搜索: 使用 search() 方法来匹配内容
import re # 引入 re 库
t_list = bs.find_all(re.compile(a)) # 正则表达式能匹配出 a 这样字样的内容, 是按照标签来找的
# re.compile() 是编译一个正则表达式对象,然后 find_all() (相当于 search()), 搜索符合正则表达式规则的内容并返回回来
print(t_list) # 由于正则表达式,会打印出所有包含 a 的内容, 打印所有匹配 a 字样的标签以及其内容, 而不是区分开来

# 3.方法: 传入一个函数(方法), 根据函数的要求来搜索
def name_is_exist(tag):
    return tag.has_attr("name") # 如果 tag 存在就返回属性, 但是这个tag 里面需要有 name 这个具体的的属性, 

t_list = bs.find_all(name_is_exist) # 所以只有有 name 这个属性的标签才会被搜索出来
print(t_list)



# 4.kwargs 参数, 指定参数来搜索
t_list = bs.find_all(id = "head") # 返回列表， 找出所有 id ="head" 的内容
# find_all()里可以给一些参数

t_list = bs.find_all(class_= True) # 只要类别里有 class 就显示出来

for i in t_list:
    print(i) # 为了更简洁明了的看内容



# 5.text 参数

t_list = bs.find_all(text = "hao123") # 找特定文本内容
t_list = bs.find_all(text = ["hao123","地图","贴吧"]) # 找特定文本内容

# 可以用正则表达式查找含有特定内容的文本
t_list = bs.find_all(text = re.compile("\d")) # 将所有含有数字的文本找出来

for i in t_list:
    print(i)


# 6.limit 参数

t_list = bs.find_all("a",limit=3) # limit 限制获取信息数量

for i in t_list:
    print(i)


# 7.css 选择器 ---> 快速定位
t_list = bs.select('title') # 返回列表, 通过标签来查找
t_list = bs.select(".mnav") # .mnav 通过类名来查找
t_list = bs.select("#u1") # 通过#id来查找
t_list = bs.select("a[class ='bri']") # 通过属性来查找, 这里就是 a 标签里的 class = 'bri' 属性
t_list = bs.select("head > title") # 找到 head 标签里的子标签 title, 通过子标签来查找

t_list = bs.select(".mnav ~ .bri") # 兄弟节点, 同级标签
print(t_list[0].gettext())

for i in t_list:
    print(i)