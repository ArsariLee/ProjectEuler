'''
第10001个质数
前6个质数分别是2、3、5、7、11和13。
第10001个质数是多少？
'''

# 依次求质数，并列表计数(下面这个耗时很久）

primeList = []
no = 0
a = 2

def isPrime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

while 1:
    if isPrime(a):
        print(a)
        primeList.append(a)
        no += 1
    a += 1
    if no = 10001:
        break

print(primeList[-1])
    

