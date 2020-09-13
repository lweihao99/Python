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


class Student(object):
    datalist = []

    def __init__(self):
        self.name = None
        self.age = None
        self.score = None
        self.address = None

    def add_student(self):
        student_info = {'name': self.name, 'age': self.age,
                        'score': self.score, 'address': self.address}
        Student.datalist.append(student_info)
        return Student.datalist

    @classmethod
    def check_info(cls):
        if len(cls.datalist) == 0:
            return "there is no info"
        check_name = input("write the name:")
        for i in cls.datalist:
            if i['name'] == check_name:
                return i['name'], i['age'], i['score'], i['address']

    @classmethod
    def del_info(cls):
        if len(cls.datalist) == 0:
            return "there is no info"

        del_name = input("enter the name who you want delete:")
        for name in cls.datalist:
            if name['name'] == del_name:
                cls.datalist.remove(name)
                return "{} deleted".format(name['name'])

    @classmethod
    def change_info(cls):
        if len(cls.datalist) == 0:
            return "nothing here"

        check_name = input("eter the name that you want to change:")
        for item in cls.datalist:
            if item['name'] == check_name:
                item['name'] = input("new name:")
                item['age'] = int(input("new age:"))
                item['score'] = int(input("new score:"))
                item['address'] = input('new address:')
                return "change success"

    @classmethod
    def rank_high_low(cls):
        cls.datalist.sort(key=lambda ele: ele['score'], reverse=True)
        print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
        for item in cls.datalist:
            print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
                  (item['name'], item['age'], item['score'], item['address']))

    @classmethod
    def rank_reverse(cls):
        cls.datalist.sort(key=lambda ele: ele['score'], reverse=False)
        print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
        for item in cls.datalist:
            print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
                  (item['name'], item['age'], item['score'], item['address']))

    @classmethod
    def student_age_high_low(cls):
        cls.datalist.sort(key=lambda ele: ele['age'], reverse=True)
        print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
        for item in cls.datalist:
            print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
                  (item['name'], item['age'], item['score'], item['address']))

    @classmethod
    def student_age_reverse(cls):
        cls.datalist.sort(key=lambda ele: ele['age'], reverse=False)
        print('\t姓名\t\t\t年龄\t\t\t成绩\t\t\t地址')
        for item in cls.datalist:
            print("\t%s\t\t\t%d\t\t\t%d\t\t\t%s" %
                  (item['name'], item['age'], item['score'], item['address']))


def main():
    student = Student()
    option = int(input("enter the number:"))
    if option == 1:
        student.name = input("enter student name:")

        for i in Student.datalist:
            if i['name'] == student.name:
                print("this name is already exists")
                main()

        student.age = int(input("enter student age:"))
        student.score = int(input("enter student score:"))
        student.address = input("enter student address:")
        print(student.add_student())
        main()

    if option == 2:
        print(student.check_info())
        main()

    if option == 3:
        print(student.del_info())
        main()

    if option == 4:
        print(student.change_info())
        main()

    if option == 5:
        student.rank_high_low()
        main()

    if option == 6:
        student.rank_reverse()
        main()

    if option == 7:
        student.student_age_high_low()
        main()

    if option == 8:
        student.student_age_reverse()
        main()

    if option == 0:
        print('end programm')
        exit(100)


if __name__ == "__main__":
    main()
