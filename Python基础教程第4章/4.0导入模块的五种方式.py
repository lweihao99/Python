'''
模块概念:
    在Python里模块本质上就是一个py文件，但不是所有py文件都能作为一个模块来导入，如果想要让一个py文件能够被导入，
    模块名字必须要遵守命名规则。


导入模块的方法:
    python 为了方便我们开发，提供了很多内置模块。
比如:
    1.import time #1， 使用 import 模块名直接导入一个模块，导入之后这个py文件里的所有方法和变量

    2.from random import randint #2， from 模块名 import 函数名， 导入一个模块里的方法或者变量，
    randint 的功能是生成随机整数
    要是没有导入random模块不能写 random.randint() 由于没有导入模块，识别不了random，而这个的意思是导入random模块里的randint方法


    3.from math import * #3. from 模块名 import * 导入这个模块里的"所有"方法和变量

    4.import datetime as dt #4. 导入一个模块并给这个模块起一个别名

    5. from copy import deepcopy as dp #5. from 模块名 import 函数名 as 别名

'''
