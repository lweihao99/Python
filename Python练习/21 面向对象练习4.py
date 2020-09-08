"""
设计两个类:
    一个类，属性包括 x,y坐标
    一个rectangle类(矩形)，属性有左上角和右下角的坐标，
        1：计算矩形的面积，
        2：判断点是否在矩形内
    实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形内
"""


class Coordinate:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, top_left: Coordinate, bottom_right: Coordinate):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def rectangle_area(self):  # 输出矩形面积
        base = self.bottom_right.x - self.top_left.x
        height = self.top_left.y - self.bottom_right.y
        area = base * height
        print('矩形面积是:', area, 'm^2')

    def is_inside(self, point):  # 判断点是不是在矩形里面
        return self.bottom_right.x >= point.x >= self.top_left.x and self.bottom_right.y <= point.y <= self.top_left.y


class Quad(Rectangle):

    def quadratic(self):
        return self.bottom_right.x % self.top_left.x == 0 and self.top_left.y % self.bottom_right.y == 0


point1 = Coordinate(3, 6)  # 定义左上角的点
point2 = Coordinate(6, 3)  # 定义右上角的点
rectangle = Rectangle(point1, point2)
rectangle.rectangle_area()

pt = Coordinate(10, 12)  # 定义点
print('点是不是在矩形里面:', rectangle.is_inside(pt))

quad = Quad(point1, point2)
print('是不是方形:', quad.quadratic())
