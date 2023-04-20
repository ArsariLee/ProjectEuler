'''
最小公倍数
2520是最小的能够被1到10整除的数。
最小的能够被1到20整除的正数是多少？
'''

'''
# 暴力穷举(1个小时没算出来）

n, j = 1, 0
while 1:
    for i in range(1, 21):
        if n % i == 0:
            continue
        j = i
        break
    if j == 20:
        print(n)
        break
    n = n + 1
'''

# 1~20，先求前两个最小公倍数，然后最小公倍数和下一个数求新的最小公倍数，已知1~10
# 最小公倍数是2520,a和b的积=最大公约数*最小公倍数，最大公约数利用辗转相除法

a = 2520
b = 1
def greatestCommonDivisor(x, y):
    if x < y:
        t = x
        x = y
        y = t
    if x % y == 0:
        return y
    else:
        return greatestCommonDivisor(y, x % y)

for i in range(11,21):
    b = greatestCommonDivisor(a, i)
    a = a * i / b
print(a)


