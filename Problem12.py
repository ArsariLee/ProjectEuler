'''
多约数的三角形数
三角形数可以由累加自然数来生成。例如，第7个三角形数是1+2+3+4+5+6+7=28。
前十个三角形数分别是：1,3,6,10,15,21,28，36,45,55...


列举出前七个三角形数的所有约数：
1:1；3:1,3；6:1,2,3，6；10:1,2,5,10；15:1,3,5,15；
21：1,3,7，21；28:1，2,4,7，14,28
可以看出，28是第一个拥有超过五个约数的三角形数。
第一个拥有超过五百个约数的三角形数是多少？
'''
# 约数个数定理：对于一个大于1正整数n可以分解质因数：n=p1^a1*p2^a2*....*pk^ak
# 则n的正约数的个数就是(a1+1)*(a2+1)*...*(ak+1)

# 分解质因数并保存（短除法）
def primeFactorization(n):
    temp = []
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                temp.append(i)
                n = n / i
                break
    return temp

# 求出列表里各质因数的个数并计算约数个数
def primeCounter(temp):
    product = 1
    counter = 1
    while 1:
        if len(temp) == 0:
            break
        counter = temp.count(temp[0])
        for i in range(counter):
            temp.pop(0)
        product = product * (counter + 1)
    return product

primeCounter(primeFactorization(21))


# 对三角形数求约数个数并输出
divisorCounter = 0
nextNum = 1
triangularNum = 0

while 1:
    triangularNum += nextNum
    divisorCounter = primeCounter(primeFactorization(triangularNum))
    print(divisorCounter)
    if divisorCounter > 500:
        print(triangularNum)
        break
    nextNum += 1





