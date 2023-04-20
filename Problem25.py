'''
1000位斐波那契数
斐波那契数列是按如下递归定义的数列：
F1=1 F2=1 Fn=F(n-1)+F(n-2)
因此斐波那契数列的前12项分别是：
F1=1 F2=1 F3=2 F4=3 F5=5 F6=8 F7=13 F8=21 F9=34 F10=55 F11=89 F12=144
第一个包含三位数字的是第12项F12。
在斐波那契数列中，第一个包含1000位数字的是第几项？
'''
# 没什么好说的
number1 = 1
number2 = 1
n = 3

while 1:
    number = number1 + number2
    number1 = number2
    number2 = number
    if len(str(number)) == 1000:
        print(n)
        break
    n += 1

    
