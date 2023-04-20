'''
圆周素数
197被称为圆周素数，因为将它逐位轮转所得到的数：197、971和719都是素数。

小于100的圆周素数有十三个：2、3、5、7、11、13、17、31、37、71、73、79和97。

小于一百万的圆周素数有多少个？
'''
#素数判断函数，同时把这个数存入列表内
primelist = []
def isPrime(a):
    if a in primelist:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    primelist.append(a)
    return True

#判断是不是圆周素数
def isCircularPrime(b):
    digits = [i for i in str(b)]
    for i in range(len(digits) - 1):
        if isPrime(int("".join(digits))):
            # 把第一个元素移到末尾
            digits.append(digits.pop(0))
        return False
    print("yes")
    return True


if __name__ == '__main__':
    count = 0
    for i in range(2, 101):
        if isCircularPrime(i):
            count += 1
    print("over",count)




    
