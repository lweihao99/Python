# 字典
# 字典区别于列表的地方，就是查找效率更高，
# 比如如果你要在12亿人里面查找某个人的身份证号码的，用列表循环的方法找人可能需要几分钟的时间，明显效率太低了，而使用字典就可以有效快速的找出来

# 语法:{key1:value1,key2:value2}
# 示例
info = {
    # {key:value}
    "name": "炜豪",
    "mission": "test dictionary",
    "email_adress": ["weihaoliu99@gmail.com", "1047828466@qq.com"],
    "university": "Biccoca",
    "age": "21",
}
print(info)

# .keys() 查找字典里所有key
print(info.keys())
# .values 查找字典里所有value
info.values()

# 取字典里的值跟元组，字符串，列表的方法一样，使用: 变量名[],只不过列表，元组，字符串是在[]写下标，而字典是写 key
print(info["email_adress"][1])

# 字典特效
# 1、字典没有下标，是 key-value 结构
# 2、key 必须为不可变数据类型，必须唯一，比如字符串，元组，数字，不能是列表因为列表是可变的
# 3、value 可任意存放多个 value，可修改，可以不唯一
# 4、字典由于是由key-value组成的，所以是无序的，而列表之所以是有序的是因为有下标
# 5、查询速度快，且不受 dict(字典) 的大小影响

# 字典的多种创建方式
# 第一种 variable = {key1:value1,key2:value2...}, 记得给key 和 value 加双引号
person = {"name:": ["name1", "name2", "name3"],
          "ages:": ["21", "29", "22"], "height": ["185", "190", "167"]}
# 第二种 variable = dict( key = "value", key = "value"), 这种方式 key　不用加双引号
person1 = dict(names="weihao", age=21)
# 第三种 variable = dict ({key:value,key2:value2})
person2 = dict({"names": "Weihao", "age": 21})
# 第四种,是批量生成默认 value 值
keys = [1, 2, 3, 4, 5, 6]
{}.fromkeys(keys)  # 这里如果在 keys 后面什么都不跟，就会默认生成 None 值来替代 value
# 所有 value = 100,{1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100}
print("默认生成value:", {}.fromkeys(keys, 100))


# 字典的增删改查

# 增
info = {
    # {key:value}
    "name:": "炜豪",
    "mission:": "test dictionary",
    "email_adress:": ["weihaoliu99@gmail.com", "1047828466@qq.com"],
    "university:": "Biccoca",
    "age:": "21",
}
print('没有追加之前:', info)
# 字典追加
info["height"] = "191cm"  # 如果字典里已经存在了，就会修改原有的 value 而不是追加新的 key-value
# .setdefault(key,value) 在字典里追加新的 key-value
info.setdefault("name", "jax")  # 如果直接打印 .setdefault 就会返回 value
info.setdefault("games", ["CSGO", "CoD", "Dota"])
# 如果创建已有 key 不会修改已有的值, 而是直接返回已有的值
print('追加之后', info)


# 删
#del 通用指令
# del info["name"] 删除key
# del info 直接删除字典

# .pop()
# info.pop("name") 删除指定 key 同 del
# .popitem() 随机删除key
# .clear() 清空 dict


# 改
# 字典追加
info["key"] = "new_value"  # 说明看第59行
# .update() 合并字典
# info.update(person), 将 person 的值加到 info 字典里
# 如果有重合的 key 就会将person 的值覆盖掉 info 里的已有key
print(info.update(person))


# 查
# 返回 True or False
print("name:" in info)
# 如果返回 True 才能查这个 key 的 value,反之会报错
# 返回 key 的 value(值)
print(info["name:"])
# .get
# 如果有这个 key 返回 value
print(info.get("name:"))
# 如果没有这个 key 返回 None, 不会报错
print(info.get("names"))
# .keys() 查找,并返回所有 key, 看第17行
# .values() 查找,并返回所有 value, 看第19行
# .items(),将 key 和 value 包含在一个大列表里，并将key 和 value 转化成一个单独的元素, 每对 key and value包含在一个元组里，而每个元组又都包含在一个大列表里
# info.items()
print("用.items", info.items())


# 循环
# 第一种循环,效率最高
# for i in info:
#     print(i)  # 这样会只打印字典里的 key
for i in info:
    print(i, info[i])  # 这样就会把 key 和 value 一起打印出来

# 第二种循环
for i in info.keys():
    print(i)  # 只打印 key

# 第三种循环
for i in info.items():
    print(i)  # 所有元组都会打印出来,整个元组
# 如果想要将元组里的元素分别打印出来,就设 2 个临时变量,如果有三个不同的元素就加3个不同的临时变量
# 如果临时变量多了会报错
for k, v in info.items():
    print(k, v)


# 求长度跟列表，字符串，元组一样
print("字典长度为:", len(info))
