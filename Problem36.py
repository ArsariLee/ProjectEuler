'''
双进制回文数

十进制数585=1001001001（二进制表示），因此它在这两种进制下都是回文数。

找出所有小于一百万，且在十进制和二进制下均回文的数，并求它们的和。

（请注意，无论在哪种进制下，回文数均不考虑前导零。）
'''
# 最终结果为872187
import time
start_time = time.time()
#回文数判断
def isPalindromic(a):
    if str(a)[-1] == "0":
        return False
    # 字符串切片操作：str(a)[::-1]代表反转
    return str(a) == str(a)[::-1]

#双进制回文数判断
def isDoubleBasePalindormes(b):
    if isPalindromic(b):
        #二进制转换（前缀会带0b表示这是二进制，所以要截掉前两位）
        return isPalindromic(bin(b)[2:])
    else:
        return False

if __name__ == '__main__':
    count = 0
    for i in range(0, 1000000):
        if isDoubleBasePalindormes(i):
            count += i
        print("已处理 %d 个数字，当前耗时 %.2f 秒" % (i+1, time.time() - start_time))
    print("处理完毕，最终结果为：", count) 
