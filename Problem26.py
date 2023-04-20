'''
倒数的循环节
单位分数指分子为1的分数。分母为2至10的单位分数的十进制表示如下所示：
1/2=0.5
1/3=0.(3)
1/4=0.25
1/5=0.2
1/6=0.1(6)
1/7=0.(142857) 
1/8=0.125
1/9=0.(1)
1/10=0.1
这里括号表示循环节，如0.1(6)就是指0.166666...，循环节的长度为1。可以看出，1/7的
循环节长度为6。
在所有满足d<1000的数中，求使得其倒数1/d的十进制表示中循环节最长的d。
'''
# 模拟除法过程将每次商和余保存，当到达某一次商余和之前相同时就代表一个循环节的结
# 束,其实倒数的循环节有更复杂的计算方式，https://zhuanlan.zhihu.com/p/377857047

def reciprocalCycles(n): # 求循环节长度
    quotient = 0 # 商
    remainder = 0 # 余
    dividend = 1 # 被除数
    saveList = []
    while 1:
        quotient = dividend // n
        remainder = dividend % n
        if not [quotient, remainder] in saveList:
            saveList.append([quotient, remainder])
        else:
            return (len(saveList) - (saveList.index([quotient, remainder])))
        dividend = remainder * 10

print(reciprocalCycles(7)) # 简单做个验证

longer = 0
d = 0
for i in range(1, 1000):
    if reciprocalCycles(i) > longer:
        longer = reciprocalCycles(i)
        d = i

print(d, longer)

    
        
        
        
