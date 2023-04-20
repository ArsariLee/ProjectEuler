'''
质数求和
所有小于10的质数的和是2+3+5+7=17。
求所有小于两百万的质数的和。
'''

# 无聊的质数求和

n = 2
sumN = 0

def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

while 1:
    if n >= 2000000:
        print(sumN)
        break
    if isPrime(n):
        print(n)
        sumN += n
    n += 1
            
