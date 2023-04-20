'''
最大回文乘积
回文数就是从前往后读和从后往前读都一样的数。由两个2位数相乘得到的最大的回文数是 。
9009=91*99
求由两个3位数相乘得到的最大的回文数。
'''

# 从100开始到999，不断循环，查看乘积是否回文数，且更新最大值

a, b = 100, 100
currentN, maxN = 0, 0

# 判断是否回文数函数
def isPalindrome(a):
    a = str(a)
    temp1=[]
    temp2=[]
    for i in range(0, len(a)):
        temp1.append(int(a[i]))
    temp2 = list(reversed(temp1))
    return(temp1 == temp2)

print(isPalindrome(1001))
print(isPalindrome(1234))

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(j * i):
            currentN = j * i
            if currentN >= maxN:
                maxN = currentN
print(currentN, maxN)
