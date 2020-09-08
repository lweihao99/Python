# 多态是基于继承的，通过重写父类的效果，达到不同的子类对象调用相同的父类方法，得到不同的结果
# 作用是提高代码的灵活度

class PoliceDog(object):  # 创建警犬类
    def attack_enemy(self):
        print('police dog is attacking an enemy')


class BlindDog(object):
    def lead_road(self):
        print('导盲犬正在领路')


class DrugDog(object):
    def search_drug(self):
        print('缉毒犬在搜毒')


class Person(object):  # 创建人类
    def __init__(self, name):
        self.name = name
        # self.dog = dog

    def work_with_pd(self):  # self指向调用方,这里就是police
        print(self.name, 'is working')
        # 由于pd是指向PoliceDog类的，所以当police调用方法的时候，self同事指向了警犬类和人类，所以可以调用pd里的方法
        self.dog.attack_enemy()

    def work_with_bd(self):
        self.dog.lead_road()

    def work_with_dd(self):
        self.dog.search_drug()


pd = PoliceDog()

# 这里的pd指向PoliceDog,然后传入dog属性,由于PersonDog里有attack_enemy，所以pd可以调用，然后police也可以调用
# police = Person('mr.Zhang', pd)
p = Person('zhangsan')
p.dog = pd  # 属性指向了pd对象
# 让狗和警察工作
p.work_with_pd()

bd = BlindDog()
p.dog = bd  # 从新又指向了别的对象，也就是bd,不再指向pd
# p.work_with_pd()  # 会报错因为bd里没有attack_enemy方法
p.work_with_bd()

dd = DrugDog()
p.dog = dd  # dog属性从新指向dd对象，不再指向bd
p.work_with_dd()

# 每添加一个类，就需要添加一个相对应的方法，然后添加新的属性，这回使得代码变得冗余，繁琐
# 这种代码不够灵活，高级所以需要使用多态
