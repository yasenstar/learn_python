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