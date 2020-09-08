# a. 小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
# b. 小美几年17岁，身高1.65，小美不跑步，小美喜欢吃东西

# 创建/定义类: 如何定义?
# 使用 class 来定义一个类
# 两种写法:
# 1.class <类名>, 一般需要遵守大驼峰命名法
# 2. class <类名>(objiect)

class Student(object):  # 关注这个类有哪些属性和行为
    # 定义属性
    def __init__(self, name, age, height):  # 在 __init__ 方法里，以参数的形式定义特征,我们称之为属性
        self.name = name
        self.age = age
        self.height = height

    # 行为定义为一个个函数
    def run(self):
        print('正在跑步')

    def eat(self):
        print('正在吃东西')


# 创建对象; 使用了Student 类创建了两个实例对象 s1 s2
# s1 s2 都会有 name,age,height 属性,同时都有 run 和 eat 方法
# Student( ) ==> 会自动调用__init__ 方法
s1 = Student('小明', 18, 1.75)  # 传参数
s2 = Student('小美', 17, 1.65)

# 对象的行为
# 根据业务逻辑，让不同的对象执行不同对的行为
s1.run()
s1.eat()

s2.eat()
