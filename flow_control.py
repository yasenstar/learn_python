# 流程控制

# num = 18
# if num > 10 and num < 20:
# 	print('num is more than 10 and less than 20')

# # 判断输入是否是管理员
# username=input("please input: ")
# print("输入的是: ", username)	    
# if username == "admin":
#     print("welcome admin coming")
# else:
#     print("wait for admin")

# input()
# print(123)

# # 判断年龄是否成年
# age = int(input("请输入你的年龄： "))
# if age >= 18:
#     print("你已经成年了")
# else:
#     print("继续成长")
# input("按任意键退出...")    

# if-elif-...-elif-else statement
# age = int(input("请输入你的年龄： "))
# if age >= 18:
#     print("你已经成年了")
# elif 0 < age < 18:
#     print("继续成长")
# else:
#     print("年龄不能是负数")
# input("按任意键退出...")  

# # 练习1：获取用户输入的整数，通过程序显示这个数是奇数还是偶数
# num = int(input("please input an integer: "))
# if num % 2 == 0:
#     print ("这是一个偶数")
# else:
#     print ("这是一个奇数")

# # 练习2：获取一个年份，判断是否是闰年
# # 如果一个年份可以被4整除而不能被100整除，或者可以被400整除，则这个年份就是闰年
# yearnum = int(input("请输入一个年份: "))
# if (yearnum % 4 == 0 and yearnum % 100 != 0 ) or (yearnum % 400 == 0):
#     print ("这是闰年")
# else:
#     print ("这是平年")

# # 判断狗🐶的年龄相当于人的多少岁
# # 狗的前两年每一年相当于人类的10.5岁，然后每增加一年就增加4岁
# import os
# dogyear = float(input("请输入你的宠物狗的年龄： "))
# if dogyear >= 2.0:
#     manyear = round(2 * 10.5 + (dogyear - 2) * 4,2)
#     print(os.getlogin(), "dogyear = ", dogyear, "manyear= ", manyear)
#     manyear = dogyear * 10.5
# elif dogyear < 2.0 and dogyear > 0:
#     manyear = round(dogyear * 10.5, 2)
#     print(os.getlogin(), "dogyear = ", dogyear, "manyear= ", manyear)
# else:
#     print("还没出生呢。。。")

# # 求100以内所以的奇数之和
# i = 0
# total = 0
# while i <= 100:
#     if i % 2 != 0:
#         total += i
#     i += 1
# print("一百以内的所有奇数之和是： ", total)

# # 求100以内的所有7的倍数之和，以及个数
# i = 0
# count = 0
# total = 0
# while i <= 100:
#     if i % 7 == 0:
#         count += 1
#         total += i
#     i += 1
# print ("一百以内的所有7的倍数的和是 ", total)
# print (" 共有 ", count, "个")

# # 水仙花数 Narcissistic Number 是指一个n位数（n>=3），其每位上的数字的n次幂之和等于它本身，求输入范围内的所有水仙花数
# i = 0
# max_num = int(input("请输入一个任意正整数： "))
# while i <= max_num:
#     if 100 <= i < 1000:
#         a = 3
#         if (i // 100 ) ** a + ((i % 100) // 10) ** a + (i % 10) ** a == i:
#             print (i)
#     i += 1

# # 判断是否是质数，即除了1和它自身以外，不能被其他自然数整除的数
# num = int(input("请给一个数来判断是否是质数(大于0的自然数)： "))
# i = 2
# a = 0
# while i < num:
#     if (num % i) == 0:
#         print ("不是质数")
#         a = i
#         i = num
#     i += 1
# else:
#     if a==0: print ("是质数")

# # 判断是否是质数，即除了1和它自身以外，不能被其他自然数整除的数 （老师的代码）2020-06-27
# num = int(input("输入一个任意的大于1的整数： "))
# i = 2
# flag = True
# while i < num:
#     if num % i == 0:
#         flag = False
#     i += 1
# if flag:
#     print(num, "是质数")
# else:
#     print(num, "不是质数")

# # 九九乘法表
# a = 1
# b = 1
# while a <= 9:
#     while b <= a:
#         print (b, "x", a, "=", a*b, " ", end="")
#         b += 1
#     print()
#     a += 1
#     b = 1

# # 九九乘法表 （老师的做法）
# i = 0
# while i < 0:
#     i += 1
#     j = 0
#     while j < i:
#         j += i
#         print(f"{j}*{i}={i*j} ", end="")    
#     print()


# 列出一定范围内的所有质数
num = int(input("请给一个数作为范围(大于0的自然数)： "))
x = 1
while x <= num:
    i = 2
    a = 0
    while i < x:
        if (x % i) == 0:
            # print ("不是质数")
            a = i
            i = x
        i += 1
    else:
        if a==0: print (x,"是质数")
    x += 1