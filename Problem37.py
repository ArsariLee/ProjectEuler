'''
可截素数
3797有着奇特的性质。它本身是一个素数；如果从左往右逐一截去数字，剩下的仍然都是素数：3797、797、97和7；

如果从右往左逐一截去数字，剩下的也仍然都是素数：3797、379、37和3。

如果一个素数满足，无论从左往右还是从右往左逐一截去数字，剩下的仍然都是素数，则称之为可截素数。

已知总共有十一个可截素数，求这些数的和。

注意：2、3、5和7不被视为可截素数。
'''
# 最终结果为748317

# 偶数肯定不是素数
# 先不确定上限，只看个数，够了11个之后，就直接结束。
import time
start_time = time.time()

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 可截素数的判断
def isTruncatablePrime(b):
    strB = str(b)
    for i in range(len(strB)):
        #从左
        if not isPrime(int(strB[i:])):
            return False
        #从右
        if not isPrime(int(strB[:len(strB)-i])):
            return False
    return True

if __name__ == '__main__':
    i = 11
    count = 0
    sum = 0
    listA = []
    while count < 11 :
        if isTruncatablePrime(i):
            listA.append(i)
            sum += i
            count += 1
            print("%d，当前耗时 %.2f 秒，已找到可截素数 %d 个" % (i, time.time() - start_time, count),listA)
        i += 2
    print("最终结果为：", sum, listA)
        

#print(isTruncatablePrime(31))
