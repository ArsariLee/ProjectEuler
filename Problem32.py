'''
全数字的乘积

如果一个n位数包含了1至n的所有数字恰好一次，我们称它为全数字的；例如，五位数15234
就是1至5全数字的。

7254是一个特殊的乘积，因为在等式39 × 186 = 7254中，被乘数、乘数和乘积恰好是1至9
全数字的。

找出所有被乘数、乘数和乘积恰好是1至9全数字的乘法等式，并求出这些等式中乘积的和。

注意：有些乘积可能从多个乘法等式中得到，但在求和的时候只计算一次。
'''

# 被乘数、乘数和乘积的数位之和为9
multiplicand = 0 # 被乘数及数位
multiplier = 0 # 乘数
product = 0 # 积
# 因为不存在0位数，所以都是从1开始穷举

def productJudge(a, b, c):
    # 关键：两数之积的位数等于两数位数之和或等于两数位数之和-1
    if a + b == c or a + b - 1 == c :
        return True
    else:
        return False

def pandigitalJudge(number1, number2, number3):
    # 对三个数整体做全数字判断，去除0
    temporaryList = []
    number1, number2, number3 = str(number1), str(number2), str(number3)
    for n in range(len(number1)):
        if number1[n] == '0':
            return False
        if number1[n] not in temporaryList:
            temporaryList.append(number1[n])
        else:
            return False
    for n in range(len(number2)):
        if number2[n] == '0':
            return False
        if number2[n] not in temporaryList:
            temporaryList.append(number2[n])
        else:
            return False
    for n in range(len(number3)):
        if number3[n] == '0':
            return False
        if number3[n] not in temporaryList:
            temporaryList.append(number3[n])
        else:
            return False
    return True

def digitCheck(digit):
    # 针对位数给出循环上下界
    returnminStr = '1'
    returnmaxStr = ''
    for n in range(digit - 1):
        returnminStr += '0'
    returnminStr = int(returnminStr)
    for n in range(digit):
        returnmaxStr += '9'
    returnmaxStr = int(returnmaxStr)
    return [returnminStr, returnmaxStr]

sumList = []

for i in range(1, 8):
    for j in range(1, 8 - i):
        k = 9 - i - j
        if not productJudge(i, j, k):
            continue
        iList = digitCheck(i)
        jList = digitCheck(j)
        kList = digitCheck(k)
        for l in range(iList[0], iList[1] + 1):
            for m in range(jList[0], jList[1] + 1):
                for n in range(kList[0], kList[1] + 1):
                    if l * m == n:
                        if pandigitalJudge(l, m, n):
                            if not n in sumList:
                                print(n)
                                sumList.append(n)

print('The sum is: ', sum(sumList))
                        
        
        
            


