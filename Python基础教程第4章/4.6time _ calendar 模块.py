# time 模块用来操作哟时间， time模块不仅可以用来显示时间，还可以控制程序，让程序暂停(使用sleep函数)
import calendar
import time

time.time()  # 获取从 1970-01-01 00:00:00 UTC 到现在的时间的秒数
time.strftime("%y-%m-%d %H:%M:%S")  # 按照指定格式输出时间
time.asctime()  # mon Apr 15 20:03:23 2019
# Mon Apr 20:03:23 2019 # 这个跟 asctime 的区别是asctime要传元组而ctime要的是秒数(时间戳)然后生成日期
time.ctime(123532)  # 但要是直接打印就是跟asctime一样的

time.sleep(0)  # 休眠


# calendar 模块是日历模块

c = calendar.calendar(2019)  # 生成2019年的日历，并且以周日为起始日期
print(c)  # 打印2019日历

calendar.firstweekday(calendar.SUNDAY)  # 设置每周起始日期码。 周一到周日分别对应 0 ~ 6
print(calendar.firstweekday())  # 返回当前每周起始日期的设置，默认情况下，首次载入calendar模块是返回0，即星期一

calendar.isleap(2000)  # 判断闰年 返回True False

calendar.leapdays(1990, 2010)  # 获取从1990到2010年一共有对少个闰年

calendar.month(2200, 3)  # 2200年3月的日历
