"""
房子(House) 有 户型，总面积，剩余面积(=总面积的60%)，和 家具名称列表属性
新房子没有任何的家具
将 家具的名称追加到家具名称列表中
判断家具的面积 是否超过剩余面积，如果超过，提示不能添加这件家具


家具(Furniture) 有 名字 和占地面积属性，其中
    席梦思(bed) 占地 4 平米
    衣柜(chest) 占地 2 平米
    餐桌(table) 占地 1.5 平米
将以上三件 家具 添加到 房子中
打印房子时 要求输出: 户型，总面积，剩余面积，家具名称列表
"""

# 创建房子类


class House(object):
    # 缺省参数直接给参数一个默认值
    # 最好不要在里面写furniture_list = []
    def __init__(self, unit_type, total_area, furniture_list=None):
        if furniture_list == None:  # 如果这个值是None 将furniture_list 设置为空列表
            furniture_list = []

        self.unit_type = unit_type  # self.属性名 = 函数参数
        self.total_area = total_area
        # 剩余面积不是直接从参数传入，而是计算出来再赋值,在创建了属性的时候就会在开辟的内存空间里创建一个属性名，所以不能为空，不然会报错
        self.remaining_area = total_area * 0.6
        self.furniture_list = furniture_list

    def add_furniture(self, x):  # 需要将家具添加到房子里，是方法
        if self.remaining_area < x.area:  # 判断剩余面积是否大于家具面积
            print('剩余面积不足，放不进去')
        else:
            # 取出家具名，因为参数x是指定到bed对象的内存空间的,也就是传入对象的内存空间
            # 由于furniture_list 是列表，所以可以用append
            self.furniture_list.append(x.name)
            self.remaining_area -= x.area  # 每次添加一个家具，就减去相应的面积

    def __str__(self):  # 这个方法必须返回字符串
        return '户型={},总面积={},剩余面积={},家具列表={}'.format(self.unit_type, self.total_area, self.remaining_area, self.furniture_list)


# 创建家具类


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建对象

# 创建房间对象的时候，传入户型和总面积
newHouse = House('four square', 20)
# 创建家具对象
sofa = Furniture('沙发', 10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 把家具添加到房间里(面向对象关注点在于:让谁做)
newHouse.add_furniture(sofa)
newHouse.add_furniture(bed)
newHouse.add_furniture(chest)
newHouse.add_furniture(table)

# 这个相当于 print(newHouse.__str__())
print(newHouse)  # print打印对象一个对象的时候，会调用这个对象的 __repr__ 或者 __str__ 方法，获取它们的返回值
