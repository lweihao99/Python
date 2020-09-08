"""
建立一个汽车类Auto,包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
至少要求汽车能够加速，减速，停车。再定义一个小汽车类CarAuto继承 Auto 并添加空调，CD属性，并且重新实现覆盖加速，减速的方法
"""


class Auto:
    def __init__(self, color, weight, wheel=4, speed=0):
        self.color = color
        self.weight = weight
        self.wheel = wheel
        self.speed = speed

    def acceleration(self, x):
        if self.speed == 0 and x <= 0:
            return  # return后面社么都没有，默认为结束进程
        self.speed += x

    def deceleration(self, x):
        self.speed -= x
        if self.speed <= 0:
            return '倒车'

    def park(self):
        return self.speed == 0


class CarAuto(Auto):
    def __init__(self, color, weight, air_conditioning, cd_player, wheel=4, speed=0):
        super().__init__(color, weight, wheel=wheel, speed=speed)
        self.air_conditioning = air_conditioning
        self.cd_player = cd_player

    def acceleration(self, x):
        return super().acceleration(x)

    def deceleration(self, x):
        return super().deceleration(x)


car_1 = Auto('yellow', '300kg')
car_1.acceleration(30)
print(car_1.speed)
car_1.deceleration(20)
print(car_1.speed)

car_2 = CarAuto('green', '500kg', 'medea', 'sony')
car_2.acceleration(50)
print(car_2.speed)
car_2.deceleration(20)
print(car_2.speed)
