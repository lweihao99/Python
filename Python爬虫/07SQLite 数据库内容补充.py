import sqlite3

# 链接数据库
conn = sqlite3.connect("test.db") # 打开或创建数据库文件
print("Opened database success")

c = conn.cursor() # 获取游标


# 创建数据表
sql = '''
    create table company 
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);

'''

'''
sql 数据类型
NULL: 值是一个NULL值
INTEGER: 值是一个带符号的整数,根据值得大小存储在1,2,3,4,6或8字节中
REAL: 值是一个浮点值,存储为8字节的IEEE浮点数字
TEXT: 值是一个文本字符串, 使用数据库编码(utf-8,utf-16BE,utf-16LE) 存储
BLOB: 值是一个blob 数据,完全根据他的输入存储
'''

c.execute(sql) # 执行sql 语句
conn.commit() # 提交数据库操作
conn.close() # 关闭数据库链接

print("成功建表")



# 插入数据

conn = sqlite3.connect("test.db")

c = conn.cursor()

sql1 ="""
    insert into company (id,name,age,address,salary)
    values (1,"张三",32,"成都",8000);
"""

sql2 ="""
    insert into company (id,name,age,address,salary)
    values (2,"张四",30,"上海",9000);
"""

c.execute(sql1)
c.execute(sql2)
conn.commit()
conn.close() # 关闭数据库链接
print("complete")



# 进行查询数据

conn = sqlite3.connect("test.db")

print("成功打开数据库")

c =conn.cursor() # 获取游标

sql = "select id,name,address,salary from company"

cursor = c.execute(sql) # 执行sql 语句

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

conn.close()



