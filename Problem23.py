'''
非盈数和
完全数是指真约数之和等于自身的数。例如，28的真约数之和为1+2+4+7+14=28，因此28是
一个完全数。
若一个数n的真约数之和小于n，则称之为亏数；反之，则称之为盈数。
由于12是最小的盈数，它的真约数之和为1+2+3+4+6=16，所以最小的能够表示成两个盈数
之和的数是24。通过数学分析可以得出，所有大于28123的数都可以被写成两个盈数的和；
尽管已知最大的不能被写成两个盈数之和的数要小于这个值，但这是仅通过分析所能得到
的最好上界。
求所有不能被写成两个盈数之和的正整数之和。
'''

# 求出小于等于28123的所有盈数，并存于列表
# 对求出的列表反复两两求和，得出一个盈数和的新列表
# 对新列表和1~28123做筛选，找出不重复的数，加起来就是所求结果

def abundant(n):
    sum1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum1 += i
    if sum1 > n:
        print(True, n, sum1)
        return True
    else:
        print(False, n, sum1)
        return False

abundantList = [i for i in range(1, 28124) if abundant(i)]
print("The longer is :", len(abundantList))
abundantSumList = []

for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
        sum2 = abundantList[i] + abundantList[j]
        if sum2 <= 28123 and (not sum2 in abundantSumList):
            abundantSumList.append(sum2)
            print(sum2)

abundantSumList.sort()
print(abundantSumList)

sum3 = 0
for i in range(1,28124):
    if i != int(abundantSumList[0]):
        sum3 += i
    else:
        abundantSumList.pop(0)
print(sum3)

# 运行时间很长，但是懒得优化了

