# 使用多态优化 5.21 的代码
class Dog:
    pass


class PoliceDog(Dog):
    def work(self):
        print('警犬正在攻击敌人')


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在引入')


class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在缉毒')


class Person:
    def __init__(self, name):
        self.name = name
        self.dog = None

    def work_with_dog(self):
        # 判断如果dog属性不是None和是Dog类实例化出来的
        if self.dog is not None and isinstance(self.dog, Dog):
            self.dog.work()


pd = PoliceDog()

p = Person('zhangsan')
p.dog = pd
p.work_with_dog()

bd = BlindDog()
p.dog = bd
p.work_with_dog()

dd = DrugDog()
p.dog = dd
p.work_with_dog()
