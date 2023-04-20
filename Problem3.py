'''
最大质因数
13195的质因数包括5、7、13和29。
600851475143的最大质因数是多少？
'''

# 短除法，从最小的质数2开始除起，每次商作为新的值继续除

n = 600851475143
temp = []

while n > 1:
    for i in range(2, int(n+1)):
        if n % i == 0:
            temp.append(i)
            n = n / i
            print(n)
            break
print(temp)
