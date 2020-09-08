import xlwt

workbook = xlwt.Workbook(encoding="utf-8") # 创建 workbook 对象, 可以理解为一个文件
worksheet = workbook.add_sheet("sheet1") # 创建工作表
# worksheet.write(0,0,'hello') # 写入数据 (0(代表行数),0(代表列数),代表参数内容)

def main ():

    worksheet.write(0,0,0)
    worksheet.write(1,0,1)
    worksheet.write(2,0,2)
    worksheet.write(3,0,3)
    worksheet.write(4,0,4)
    worksheet.write(5,0,5)
    worksheet.write(6,0,6)
    worksheet.write(7,0,7)
    worksheet.write(8,0,8)
    worksheet.write(9,0,9)


    worksheet.write(0,1,1)
    worksheet.write(0,2,2)
    worksheet.write(0,3,3)
    worksheet.write(0,4,4)
    worksheet.write(0,5,5)
    worksheet.write(0,6,6)
    worksheet.write(0,7,7)
    worksheet.write(0,8,8)
    worksheet.write(0,9,9)

    for i in range(1,10): # 99乘法表
        for k in range(1,10):
            num = i * k
            worksheet.write(i,k,num)
    
    workbook.save("./student.xls")


if __name__ == "__main__":
    main()  



