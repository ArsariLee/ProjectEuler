'''
数字阶乘和

145是个有趣的数，因为1!+4!+5!=1+24+120=145。

找出所有各位数字的阶乘和等于其本身的数，并求它们的和。

注意：因为1!=1和2!=2不是和的形式，所以它们并不在讨论范围内。
'''

# 首先要确定数字范围的上限，直觉可以想到一定会到了某个数之后，阶乘和无论如何都赶不上数字本身的大小。
# 导入math，阶乘使用math.factorial()计算
import math
# 预先计算0~9的阶乘值，并存储到字典中
factorials = {str(i): math.factorial(i) for i in range(10)}
# 定义一个计算阶乘和的函数
def factorialSum(n):
    return(sum(map(lambda x:factorials[x], str(n))))

# 9!=362880,阶乘和最大的情况只出现在99、999、9999、99999这样的数中，8位数是千万量级，而8*362880只有百万。所以数字上限限定在99999999
# 通过计算不等式可以将范围进一步缩小到7位数

def numSum():
    sum1 = 0
    for i in range(3, 10000000):
        if i == factorialSum(i):
            sum1 += i
            print(i, sum1)
    print(sum1)


if __name__ == "__main__":
    numSum()
    print('over')
    #答案是 40730