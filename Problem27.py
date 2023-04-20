'''
素数生成二次多项式
欧拉发现了这个著名的二次多项式：
n²+n+41
对0≤n≤39范围内的所有整数，这个多项式可以生成40个质数。但是，当n=40时，
40²+40+41=40(40+1)+41能够被整除，而当n=41时，41²+41+41显然也能够被41整除。

之后，人们又发现了一个神奇的多项式n²-79n+1601，这个多项式能够对0≤n≤79范围内的
所有整数生成80个质数。这个二次多项式的系数分别是-79和1601，其乘积为-126479。

考虑所有如下形式的二次多项式：
n²+an+b，其中|a|<1000，|b|≤1000；这里|n|表示n的绝对值，例如|11|=11，|-4|=4。
找出其中能够从n=0开始连续生成最多素数的二次多项式表达式，并给出其系数a和b的乘积。
'''
# 进行一个暴力的解

primesList = [] # 创建一个存放素数的列表，减少素数检查时的计算量

def primeJudge(numPrime): # 素数判断及列表更新
    if numPrime < 1:
        return False
    if numPrime in primesList:
        return True
    for i in range(2, numPrime):
        if numPrime % i == 0:
            return False
    if not (numPrime in primesList):
        primesList.append(numPrime)
        return True
    else:
        return True

def quadraticPrimesJudge(numa, numb): #多项式生成检查
    numn = 0
    numnew = 0
    count = 0 # 生成素数的个数
    while 1:
        numnew = numn ** 2 + numa * numn + numb
        if primeJudge(numnew):
            numn += 1
            count += 1
        else:
            return count
        
print(quadraticPrimesJudge(-79,1601)) # 简单做个验证
      
maxCount = 0
maxList = [0, 0, 0, 0]
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if quadraticPrimesJudge(a, b) > maxCount:
            maxCount = quadraticPrimesJudge(a, b)
            maxList = [maxCount, a, b, a*b]
            print(maxList)
print("最终结果：", maxList[-1])
        
        
        
