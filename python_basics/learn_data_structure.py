# # 字符串普通创建方式
# str1='你好世界'
# print(str1)
#
# # 字符串转换
# a=1
# str_trans=str(a)
# print(str_trans)
# print(type(str_trans))
from os.path import join

# 字符串添加，可以使用+拼接，也可以使用 join()来处理
# str='hello'
# str2=str+' world!'
# print(str2)
# print('添加前字符串 id:',id(str))
# print('添加后字符串 id:',id(str2))
# print('2个字符串的 id 是否相等：', id(str) is id(str2))
# print(f"2个字符串是同一个对象吗？{str is str2}")
# # 这是拼接字符串，不是比较
# print(f"2个字符串是同一个对象吗？{str} is {str2}")


# join 添加
# parts=[]
# for i in range(10):
#     # TypeError: sequence item 0: expected str instance, int found 报错信息
#     # parts.append(i)
#     # IndexError: string index out of range
#     # parts.append(str[i])
#     # 目的是需要将数字转换为字符串，所以这里要用 str()方法
#     parts.append(str(i))
# str_join=','.join(parts)
# print(str_join)

# +拼接数据耗时对比 join拼接数据耗时，结论:join比+拼接快，原因是 join是在拼接的最后才生成 1 个字符串，+拼接是每次拼接都会产生一个字符串，数据多时，就会产生大批量字符串


# # join 耗时为： 1.270488977432251 (效率高)
# import time
# start_time=time.time()
# parts=[]
# for i in range(10000000):
#     parts.append(str(i))
# str_join=",".join(parts)
# # print(str_join)
# end_time=time.time()
# print("耗时为：", end_time-start_time)

# # +拼接 耗时为： 1.397956132888794（效率低）
# import time
# start_time=time.time()
# parts=[]
# for i in range(10000000):
#     # 循环里拼接字符串使用+=在循环里拼接就可以
#     parts += str(i)
# end_time=time.time()
# print("耗时为：", end_time-start_time)


# # 删除
# str='hello,world'
# # 表示替换为空，但是单引号之间是没有空格的，所以可以代表删除，当然也可以替换其他数据，比如：str2=str.replace(',','1233')
# str2=str.replace(',','')
# print(str2)


# # 移除特定字符串
# str='   hello   ,world!   '
# str2=str.strip()
# print(str2)
# # 输出结果为：hello   ,world
# # 原因：stripe()只可以移除左右两边的空格
#
# str3=str.lstrip()
# print(str3)
#
# str4=str.rstrip()
# print(str4)
#
# str5=str.replace(' ','')
# print(str5)


# # 移除特定字符串 2
# str='&&&hello,&&world!***'
# str2=str.replace('&','')
# print(str2)
# str3 = str2.replace('*','')
# print(str3)


# # 获取单个元素
# str='hello world'
# print(str[0])


# # 获取多个元素
# str='hello world'
# # 获取某个区间的元素，需要使用:来分隔
# # str2=str[0,2]
# # 注意：左闭右开
# str2=str[0:2]
# print(str2)
# # 输出结果：he

# # 遍历
# str='hello world'
# for i in str:
#     print(i)

# 修改

# # 修改方式 1：创建新字符串，通过+拼接切片进行连接
# str='hello world'
# str2='H'
# str3=str2+str[1:12]
# print(str3)

# 修改方式 2: 转换为列表，在转换为字符串
# str='hello world'
# list = list(str)
# list[0]='H'
# print(list)
# str2=''.join(list)
# print(str2)


# # 字符串大小写转换
# str='hello world'
# str2=str.upper()
# print(str2)
#
# str3='HELLO WORLD'
# str4=str3.lower()
# print(str4)
#
# str5=str.title()
# print(str5)


# 字符串长度
str='hello world'
print(len(str))