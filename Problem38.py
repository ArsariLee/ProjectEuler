'''
全数字的倍数
将192分别与1、2、3相乘：
192*1=192
192*2=384
192*3=576
将这些乘积拼接起来，可以得到一个1至9全数字的数192384576，因此称192384576为192和(1,2,3)的拼接乘积。

类似地，将9分别与1、2、3、4、5相乘，可以得到1至9全数字的数918273645，并称之为9和(1,2,3,4,5)的拼接乘积。

考虑所有n>1时某个整数和(1,2,...,n)的拼接乘积，其中最大的1至9全数字的数是多少？
'''

# 最终结果为932718654

# 从1开始，和（1,n)相乘，乘的时候拼接，在等于9位的时候检查有无重复元素以及0
# 关于上限，n最小为2，所以最多只能到9999（如果五位数的话，无论如何拼接结果都大于9位了）

def PandigitalMultiples(a):
    strA = ''
    i = 1
    while len(strA) < 9 :
        strA += str(a*i)
        i += 1
    if len(strA) != 9 or '0' in strA:
        return False
    if all(j in strA for j in '123456789'):
        print(strA, a)
        return int(strA)

if __name__ == '__main__':
    m = 0
    for k in range(1, 10000):
        result = PandigitalMultiples(k)
        if result and result >= m:
            m = result       
    print('over', m)




