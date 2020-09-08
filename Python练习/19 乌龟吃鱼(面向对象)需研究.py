"""
乌龟吃鱼：
假设游戏场景为范围（x，y）为0<=x<=10,0<=y<=10
游戏生成1只乌龟和10只鱼,他们的移动方向随机
乌龟的最大移动能力为2（它可以随机选择1或2）,鱼的最大移动能力是1
当移动到边缘时，自动向反方向移动
乌龟的初始体能为100（上限）
乌龟每移动一次体能-1
当乌龟与鱼的坐标重叠时，鱼被乌龟吃掉，乌龟体力加20
鱼暂不计体能
当乌龟体能为0（挂掉）或鱼被吃光，游戏结束
"""
import random


class Trutle(object):
    # 构造函数何时执行？类实例化对象(创建对象)时，自动调用该函数内容
    def __init__(self):
        # 随机生成乌龟的坐标
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        # 乌龟初始化体力为100（上限）
        self.power = 100

    def move(self):
        # 乌龟的最大移动能力为2
        move_skill = [-2, -1, 0, 1, 2]

        # 计算出乌龟新的坐标; (10,0)  (12,0)
        new_x = self.x + random.choice(move_skill)  # 12
        new_y = self.y + random.choice(move_skill)  # 0

        # 更新乌龟的坐标值
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

        # 乌龟每移动一次，体力消耗1
        self.power -= 1

    def is_vaild(self, value):  # 12
        """判断坐标值是否合法(0~10之间), 返回合法的值"""
        if value < 0:  # eg: -2 ==   abs(-2) ==> 2
            return abs(value)
        elif value > 10:  # eg: 12 ====>   10-(12-10)  ==> 8
            return 10 - (value - 10)
        return value

    def eat(self):
        # 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
        self.power += 20


class Fish(object):
    def __init__(self):
        # 随机生成鱼的坐标
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        # 鱼的最大移动能力为1
        move_skill = [-1, 0, 1, ]
        # 计算出鱼新的坐标; (10,0)  (12,0)
        new_x = self.x + random.choice(move_skill)  # 12
        new_y = self.y + random.choice(move_skill)  # 0

        # 更新鱼的坐标值
        self.x = self.is_vaild(new_x)
        self.y = self.is_vaild(new_y)

    def is_vaild(self, value):  # 12
        """判断坐标值是否合法(0~10之间), 返回合法的值"""
        if value < 0:  # eg: -2 ==   abs(-2) ==> 2
            return abs(value)
        elif value > 10:  # eg: 12 ====>   10-(12-10)  ==> 8
            return 10 - (value - 10)
        return value


def start_game():
    # 创建一个乌龟
    t1 = Trutle()
    # 创建10个鱼
    # fishs = []
    # for i in range(10):
    #     fishs.append(Fish())
    fishs = [Fish() for i in range(10)]
    # 游戏开始运行
    while True:
        # 判断游戏是否结束(乌龟没体力或者鱼被吃光了)
        if t1.power <= 0:
            print("乌龟没体力了， Game over.........")
            break
        elif len(fishs) == 0:
            print("鱼被吃光了， Game over......... ")
            break
        else:
            # 乌龟和鱼随机移动
            t1.move()
            for index, fish in enumerate(fishs):
                fish.move()
                # 判断乌龟是否吃到了鱼？
                if t1.x == fish.x and t1.y == fish.y:
                    t1.eat()
                    fishs.remove(fish)
                    print("鱼被吃掉， 还剩%d条鱼......." % (len(fishs)))
                    print("乌龟最新体能为%s" % (t1.power))
            # 当乌龟的坐标与每一条鱼进行比较，都没有重合，也就是没有吃到一条鱼;
            else:
                print("乌龟没有吃到鱼，最新体能为%s" % (t1.power))


# 如果这个脚本(模块)，没有被调用，则执行下面的代码
if __name__ == "__main__":
    print("游戏开始".center(50, '*'))
    start_game()
