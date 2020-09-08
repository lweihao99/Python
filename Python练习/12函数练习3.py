# 函数,检查传入字典的每一个 value 的长度, 如果大于2,那么仅保留前两个长度的内容,并将新内容返回给调用者. PS：字典中的value 只能是字符串或列表
def funcDict(**dictPargraph):
    # 定义一个新空字典,用来返回新字典
    result = {}
    # 判断key 和 value 的长度
    # .items 将key 和 value 转化成一个单独的元素,返回字典里所有元素,并且每对元素都包含在一组元组里,每组元组都包含在一个大列表里,大列表外面就是一大元组
    for key, value in dictPargraph.items():
        if len(key) > 2:  # 如果value 长度 >2
            # 切片
            value[:2]
            # 往字典里追加数据
            # 追加新的 key - value
            result[key] = value[:2]
        else:  # 给新字典所有内容
            result[key] = value
    # 返回值返回给函数调用
    return result


# 函数调用
fDict = {"name": "Weihao", "兴趣": [
    "打游戏", "听歌", "学习"], "Age": "21", "Height": "1.85", "Weight": "67"}
print(funcDict(**fDict))  # 只会打印 value 的前两个下标元素
