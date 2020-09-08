# 名片管理系统

def main():  # 主程序
    print('名片管理系统 v1.0'.center(50, '-'))
    msg = '''
    1: 添加名片
    2: 删除或修改名片
    3: 查询名片
    4: 显示所有名片

    0: 退出系统
    '''
    print(msg)
    print('END'.center(50, '-'))

    enter = int(input('请输入你要进行的操作:'))
    while True:
        if enter == 1:  # 添加名片

            print(add())
            print('用户添加成功')
            print('END'.center(100, '-'))
            main()

        elif enter == 2:  # 修改，删除
            modify()
            main()

        elif enter == 3:  # 查询
            search()
            main()

        elif enter == 4:  # 显示
            display()
            main()

        elif enter == 0:  # 退出系统
            print('你确定要结束程序吗?')
            enter = input("输入yes or no:")
            if enter == 'yes':
                print('程序已退出')
                exit(0)
            elif enter == 'no':
                main()

        else:
            print('抱歉没有这个功能')
            break


dataList = []  # 防止之前添加的名片信息丢失,存储用户名


def add():  # 添加名片

    print('Add'.center(100, '-'))
    name = input('请输入姓名:')
    for item in dataList:  # 判断此用户是否已被注册
        if item['name'] == name:
            print('此用户名已被注册，请重新输入')
            main()

    tel = input('请输入手机号:')
    qq = input('请输入QQ号:')
    email = input('请输入邮箱地址:')

    info = {'name': name, 'tel': tel, 'qq': qq, 'email': email}
    dataList.append(info)
    return dataList


def modify():  # 删除名片

    global dataList
    print('修改名片'.center(50, '-'))

    if len(dataList) == 0:
        print('对不起，目前没有数据可以更改')
        main()

    enter = input("修改写change,删除写remove:")
    if enter == 'remove':
        for i in dataList:
            check = input("请输入你要删除的名字:")
            if check == i['name']:
                dataList.remove(i)
                break
    if enter == 'change':
        for i in dataList:
            change = input('请输入你要修改的名字:')
            if change == i['name']:
                i['name'] = input('请输入新的名字:')
                i['tel'] = input('请输入新的电话号码:')
                i['qq'] = input('请输入新的QQ号码:')
                i['email'] = input('请输入新的邮箱地址:')

                print('%s的名片修改成功' % (i['name']))
                break

    print('END'.center(100, '-'))


def search():  # 名片信息查询

    print('Search'.center(100, '-'))
    findName = input("请输入你要找的姓名:")

    for item in dataList:
        if item['name'] == findName:
            print("姓名\t\t\t\t电话\t\t\t\tQQ\t\t\t\t邮箱")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" %
                  (item['name'], item['tel'], item['qq'], item['email']))
            break

    else:  # 这个不能再for循环下面，因为for循环会把所有元素都遍历一遍，每次 遍历的元素不是我要找的话，就会打印出没有找到
        print('没有找到:%s' % findName)

    print('END'.center(100, '-'))


def display():  # 遍历循环字典里的信息

    print('显示所有名片信息'.center(100, '-'))
    if len(dataList) == 0:
        print('对不起,目前没有任何数据')
    else:
        # for i in dataList: # 打印所有已经存储的信息
        #     print(i) # 这种方法打印出来不好看，可以用表格的方式打印出来
        for name in ['姓名', '电话', 'QQ', '邮箱']:
            print(name, end="\t\t\t\t")  # 将4个列表名分隔开来
        print('')
        print('='*100)  # 分割线

        for i in dataList:  # 遍历出的i是整个字典
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" %
                  (i['name'], i['tel'], i['qq'], i['email']))  # 将每个数据都放到对的地方

    print('END'.center(100, '-'))


if __name__ == '__main__':

    main()
