'''
字典序排列
排列指的是将一组物体放置为特定的顺序。例如，3124是数字3、1、2、4的一个排列。将所
有排列按照数字大小或字母先后进行排序称为字典序。数字0、1、2的字典序排列是：
012 021 102 120 201 210
在数字0、1、2、3、4、5、6、7、8、9的字典序排列中，处于第一百万位的排列是什么？
'''

# 10位数有10！种排列方式,从第1位开始排列，第1位有10种选择，每种选择对应9!种排列
# 一百万对9！取模，即可知道第1位是多少，而且是对应的9！里第几位排列。
# 按照这个思路连续取模下去，最终就能确定第一百万位排列

def factorial(n):
    product = 1
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            product *= i
        return product


def permutations(n):
    # 创建0~9数字列表
    numberList = [i for i in range(10)]
    # 存放最终排列
    strList = []
    
    for i in range(1,10):
        # 向下取整得出商的整数部，然后取模
        digit = n // factorial(len(numberList) - 1)
        n = n % factorial(len(numberList) - 1)
        # 求出当前第i位对应的数字
        if n != 0 :
            digit += 1
        strList.append(numberList[digit - 1])
        # 从列表里剔除已经选出的数字
        numberList.pop(digit - 1)
        print(digit, n, numberList)
    # 把最后剩下的数字放到末尾
    strList.append(numberList[0])
    print(strList)

permutations(1000000)
    
