# 开放封闭原则

def can_play(fn):
    def inner(name,game,*args,**kwargs):
        # print(args)
        clock = kwargs.get('clock',23) # clock是拿的key，23是默认值，.get是为了避免字典的bug
        if clock <= 22:
            fn(name,game)
        else:
            print('太晚了，赶紧睡')
    
    return inner


@can_play # 装饰器用法
def play_game(name,game):

    print('{}正在玩游戏{}'.format(name,game))


play_game('张三','王者荣耀', clock = 23)
play_game('李四','绝地求生',23)