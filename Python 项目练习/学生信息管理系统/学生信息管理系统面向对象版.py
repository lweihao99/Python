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

    def change_info(self):
        pass

    def rank_high_low(self):
        pass

    def rank_reverse(self):
        pass

    def student_age_high_low(self):
        pass

    def student_age_reverse(self):
        pass


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


main()
