'''
亲和数
记d(n)为n的所有真约数（小于n且整除n的正整数）之和。如果d(a)=b且d(b)=a，且a≠b，
那么a和b构成一个亲和数对，a和b被称为亲和数。
例如，220的真因数包括1、2、4、5、10、11、20、22、44、55和110，因此d(220)=284；
而284的真因数包括1、2、4、71和142，因此d(284)=220。
求所有小于10000的亲和数的和。
'''

# 求d
def d(n):
    sumd = 0
    for i in range(1, n):
        if n % i == 0 and n > i:
            sumd += i
    return sumd

# 存10000以内各数真约数之和
dN = [d(i) for i in range (10000)]

# 判断亲和数并存列表
listAmicableNumbers = []
for i in range(10000):
    for j in range(10000):
        if i == dN[j] and dN[i] == j and i != j:
            if listAmicableNumbers.count(i) < 1 and listAmicableNumbers.count(j) < 1:
                listAmicableNumbers.append(i)
                listAmicableNumbers.append(j)
print(listAmicableNumbers)
print(sum(listAmicableNumbers))        

