'''
整数边长直角三角形
考虑三边长{a,b,c}均为整数的直角三角形，并记其周长为p，当p = 120时，恰好存在三个不同的解
[20,48,52},{24, 45, 51}, {30, 40, 50}
在所有的p≤1000中，p取何值时有最多个解?
'''

# a+b=p-c --->  ab=(p²-2pc)/2
# a+b>c   --->  c<p/2
# c>b ,ac>ab ---> a > (p²-2pc)/2c  , c > a --->  c > p/(1+√3)
# 斜边的上下范围已定      (p/(1+√3) , p/2)   
# 直角边的上下范围已定    ((p²-2pc)/2c , c)
# 均不包含
# 然后穷举吧

import math

# solveTri函数里要先计算a的范围
def aRange(num_p, num_c):
    num_min = math.ceil(((num_p ** 2) - (2 * num_p * num_c)) / (2 * num_c))
    num_max = num_c - 1
    return num_min, num_max


def solveTri(p):
    solutions=[]
    #设定c的范围
    c_min = math.ceil(p / (1 + 3 ** 0.5))
    c_max = math.floor(p / 2)
    for c in range(c_min, c_max + 1):
        #设定a的范围
        a_min, a_max = aRange(p, c)
        for a in range(a_min, a_max + 1):
            b = p - a - c
            if a**2 + b**2 != c**2 or a==0 or b==0 or c==0:
                continue
            else:
                solutions.append([a,b,c])
    print(solutions)
    #懒得研究怎么去重了，先除以2吧。
    return len(solutions)/2

if __name__ == '__main__':
    max_num = 0
    for i in range(1, 1001):
        currentNum = solveTri(i)
        max_num = max(max_num, currentNum)
    print(max_num)

# 最终答案为8


    
