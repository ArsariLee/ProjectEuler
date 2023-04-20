'''
圆周素数
197被称为圆周素数，因为将它逐位轮转所得到的数：197、971和719都是素数。

小于100的圆周素数有十三个：2、3、5、7、11、13、17、31、37、71、73、79和97。

小于一百万的圆周素数有多少个？
'''
# 答案是55
import time
start_time = time.time()
#素数判断函数，同时把这个数存入列表内
primelist = [2] #提前存2
def isPrime(a):
    if a <= primelist[-1]:
        return a in primelist
    for i in range(primelist[-1] + 1, a + 1):
        # 生成表达式，如果一个数能被素数整除，那他就一定不是素数
        if all(i % p != 0 for p in primelist):
            primelist.append(i)
    return a in primelist

#判断是不是圆周素数
def isCircularPrime(b):
    digits = [i for i in str(b)]
    for i in range(len(digits)):
        if not isPrime(int("".join(digits))):
            return False
        # 把第一个元素移到末尾
        digits.append(digits.pop(0))    
    return True


if __name__ == '__main__':
    count = 0
    for i in range(2, 1000000):
        if isCircularPrime(i):
            count += 1
        # 增加print会增加耗时
        print("已处理 %d 个数字，当前耗时 %.2f 秒" % (i, time.time() - start_time))
    end_time = time.time()
    print("over",count)
    print("处理完毕，用时：", end_time - start_time)





    
