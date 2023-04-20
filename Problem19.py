'''
周日计数
下列信息是已知的，当然你也不妨自己再验证一下：
1990年1月1日是周一。
三十天在九月中，
四六十一也相同。
剩下都是三十一，
除去二月不统一。
二十八天平常年，
多加一天在闰年。
闰年指的是能够被4整除却不能被100整除，或者能够被400整除的年份。
在二十世纪（1901年1月1日到2000年12月31日）中，有多少个月的1号是周日？
'''

# 1901年1月1号周2
week = 1
month = 1
days = 31
year = 1901
sundayCounter = 0

def isLeapYear(a):
    if a % 400 == 0:
        return True
    elif a % 4 == 0 and a % 100 != 0:
        return True
    else:
        return False

while 1:
    for month in range(1, 13):
        if month == 4 or month == 6 or month == 9 or month == 11:
            days = 30
        elif month == 2:
            if isLeapYear(year):
                days = 29
            else:
                days = 28
        else:
            days = 31

        for i in range(1, days + 1):
            if week == 7:
                week = 1
            else:
                week += 1
                if week == 7 and i == 1:
                    sundayCounter += 1
    year += 1
    if year == 2001:
        print(sundayCounter)
        break
    
        
        
