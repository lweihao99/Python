import xlwt

'''
1) 添加学生信息
2) 查看学生信息
3) 删除学生信息
4) 修改学生成绩
5) 按学生成绩从高到低显示学生信息
6) 按学生成绩从低到高显示学生信息
7) 按学生年龄从高到低显示学生信息
8) 按学生年龄从低到高显示学生信息
0) 退出

exel数据保存

学生的信息有: 姓名，年龄，成绩，住家地址
'''


def main():  # 主程序
    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生信息管理系统'+' '*41+'|')
    print('+'+'-'*100+'+')

    menu()  # 调用菜单选项

    enter = input('请输入对应指令:')
    savePath = r"./学生管理系统.xls"  # exel数据表格保存路径

    if enter == '1':  # 添加学生信息
        print(addStudents())
        main()

    elif enter == '2':  # 查看学生信息
        display()
        main()

    elif enter == '3':  # 删除学生信息
        delete()
        main()

    elif enter == '4':  # 修改学生信息
        modify()
        main()

    elif enter == '5':  # 按学生成绩从高到低显示学生信息
        scoreRatingHigh()
        main()

    elif enter == '6':  # 按学生成绩从低到高显示学生信息
        scoreRatingLow()
        main()

    elif enter == '7':  # 按学生年龄从高到低显示学生信息
        pass

    elif enter == '8':  # 按学生年龄从低到高显示学生信息
        pass

    elif enter == '9':  # 查看所有学生信息，顺序以添加时间为准
        showAll()
        main()

    elif enter == '0':  # 退出
        out()

    elif enter == "save":
        saveData(savePath)

    elif enter == "modify exel":
        exelModify()

    else:
        print('抱歉，目前还没有这个功能...')
        main()


def menu():  # 可操作指令
    msg = '''
    1: 添加学生信息
    2: 查看学生信息
    3: 删除学生信息
    4: 修改学生信息
    5: 按学生成绩从高到低显示学生信息
    6: 按学生成绩从低到高显示学生信息
    7: 按学生年龄从高到低显示学生信息
    8: 按学生年龄从低到高显示学生信息
    9: 查看所有学生信息

    0: 退出

    输入save保存到exel数据表格
    输入modify，修改exel表格
    '''
    print(msg)
    print('+'+'-'*100+'+')
    print('|'+' '*48+'END'+' '*49+'|')
    print('+'+'-'*100+'+')


infos = []  # 存储学生所有信息


def addStudents():  # 添加学生信息

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生信息添加'+' '*45+'|')
    print('+'+'-'*100+'+')

    name = input('请输入学生姓名:')
    age = int(input('请输入学生年龄:'))
    score = int(input('请输入学生成绩:'))
    address = input('请输入学生住家地址:')

    for item in infos:  # 判断学生是否以及注册过了
        if item['names'] == name:
            if item['ages'] == age:
                if item['address'] == address:
                    print('这个学生已经注册过了...')
                    main()

    info = {'names': name, 'ages': age,
            'score': score, 'address': address}  # 单个学生信息
    infos.append(info)  # 将每条录取信息存储到总列表里

    print('+'+'-'*100+'+')
    print('|'+' '*44+'信息添加成功'+' '*44+'|')
    print('+'+'-'*100+'+')

    return infos


def display():  # 查看数据

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*45+'查看学生信息'+' '*43+'|')
    print('+'+'-'*100+'+')

    if len(infos) == 0:
        print("抱歉,目前没有录取任何信息....")

    enter = input("\n请输入你要查找的学生姓名:")
    print('-'*100)

    for name in infos:
        if name['names'] == enter:
            print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
            print('\t%s\t\t\t%d\t\t\t%d\t\t\t%s' %
                  (name['names'], name['ages'], name['score'], name['address']))
            break
    else:
        print('抱歉，没有你要找的人....')
        main()

    print('+'+'-'*100+'+')
    print('|'+' '*48+'END'+' '*49+'|')
    print('+'+'-'*100+'+')


def delete():  # 删除学生信息和修改学生信息

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*44+'删除学生信息'+' '*44+'|')
    print('+'+'-'*100+'+')

    if len(infos) == 0:
        print("抱歉，目前没有任何信息可供删除....")
        main()

    for name in infos:
        search = input("请输入你要移除的人名:")
        if name['names'] == search:
            infos.remove(name)  # 移除指定人名
            print('+'+'-'*100+'+')
            print('|'+' '*41+'该信息已被成功移除'+' '*42+'|')
            print('+'+'-'*100+'+')
            break


def modify():  # 修改信息

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*44+'修改学生信息'+' '*44+'|')
    print('+'+'-'*100+'+')

    if len(infos) == 0:
        print("抱歉，目前没有任何信息可供修改....")
        main()

    for name in infos:
        search = input("请输入你要修改的名字:")
        if name['names'] == search:
            print("找到了该学生信息...")

            name['names'] = input("请输入新的姓名:")
            name['ages'] = int(input("请输入新的年龄:"))
            name['score'] = int(input("请输入新的成绩:"))
            name['address'] = input("请输入新的地址:")
            print("修改完成....")

            print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
            print('\t%s\t\t\t%d\t\t\t%d\t\t\t%s' %
                  (name['names'], name['ages'], name['score'], name['address']))

            break

        else:
            print("抱歉，没有找到该人名...")
            break

    print('+'+'-'*100+'+')
    print('|'+' '*48+'END'+' '*49+'|')
    print('+'+'-'*100+'+')


def scoreRatingHigh():  # 按学生成绩从高到低显示

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生成绩从高到低'+' '*43+'|')
    print('+'+'-'*100+'+')

    # 使用reverse 将排序反转,原来的排序是从低到高
    infos.sort(key=lambda ele: ele['score'], reverse=True)

    print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
    for item in infos:
        print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
              (item['names'], item['ages'], item['score'], item['address']))
    return infos


def scoreRatingLow():  # 按学生成绩从低到高显示

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生成绩从低到高'+' '*43+'|')
    print('+'+'-'*100+'+')

    # 使用reverse 将排序反转,原来的排序是从低到高
    # infos.sort(key=lambda ele: ele['score'], reverse=False)
    rating = sorted(infos, key=lambda ele: ele['score'], reverse=False)
    print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
    for item in rating:
        print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
              (item['names'], item['ages'], item['score'], item['address']))


def ageHigh():  # 按学生年龄从高到低显示,现在以年龄为准，之后可以以生日为准

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生年龄从高到低'+' '*43+'|')
    print('+'+'-'*100+'+')

    infos.sort(key=lambda ele: ele['ages'], reverse=True)  # 年龄排序
    print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
    for item in infos:
        print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
              (item['names'], item['ages'], item['score'], item['address']))


def ageLow():  # 按学生年龄从低到高显示

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'学生年龄从低到高'+' '*43+'|')
    print('+'+'-'*100+'+')

    infos.sort(key=lambda ele: ele['ages'], reverse=False)  # 年龄排序
    print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
    for item in infos:
        print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
              (item['names'], item['ages'], item['score'], item['address']))


def showAll():  # 查看所有学生信息

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'查看所有学生信息'+' '*41+'|')
    print('+'+'-'*100+'+')

    if len(infos) == 0:
        print('抱歉，目前数据库没有录取任何信息...')
        main()
    print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
    for item in infos:
        print('\t%s\t\t\t%d\t\t\t%d\t\t\t%s' %
              (item['names'], item['ages'], item['score'], item['address']))

    print('+'+'-'*100+'+')
    print('|'+' '*48+'END'+' '*49+'|')
    print('+'+'-'*100+'+')


def saveData(savePath):  # exel数据保存

    print('')
    print('+'+'-'*100+'+')
    print('|'+' '*43+'开始保存学生信息'+' '*41+'|')
    print('+'+'-'*100+'+')

    # 开始创建exel文件
    book = xlwt.Workbook(encoding="UTF-8", style_compression=0)
    sheet = book.add_sheet("学生信息表", cell_overwrite_ok=True)
    colums = ("学生姓名", "学生年龄", "学生成绩", "学生地址")

    for i in range(0, 4):  # 列名
        sheet.write(0, i, colums[i])

    for i in range(0, len(infos)):  # 将数据列出来，并保存
        data = infos[i]
        sheet.write(i+1, 0, data['names'])
        sheet.write(i+1, 1, data['ages'])
        sheet.write(i+1, 2, data['score'])
        sheet.write(i+1, 3, data['address'])

    book.save(savePath)
    print("保存完毕")


def exelModify():  # 在已有的数据表格上修改
    pass


def out():  # 退出程序

    answer = input('你确定你要退出么?\n请输入 yes 或者 no:')

    if answer == 'yes':
        print('程序正在退出...')
        exit(0)
    elif answer == 'no':
        main()
    else:
        print('没有这个指令..')
        print('请重新输入...')
        out()


if __name__ == "__main__":  # 主程序入口

    main()
