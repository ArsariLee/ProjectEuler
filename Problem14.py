'''
最长考拉兹序列
考虑如下定义在正整数集上的迭代规则：
 n->n/2（若为偶数）n->3n+1 （若为奇数）
从13开始，可以迭代生成如下的序列：
13-40-20-10-5-16-8-4-2-1
可以看出这个序列（从13开始到1结束）共有10项。
尽管还未被证明，但普遍认为，从任何数开始最终都能回到1（这被称为“考拉兹猜想”）。
在小于一百万的数中，从哪个数开始迭代生成的序列最长？
注： 在迭代过程中允许出现超过一百万的项。
'''

# 挨个算
def collatzRule(n):
    count = 1
    while n > 1:        
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        count += 1
    return count

print(collatzRule(13))

maxCount = 1
currentCount = 1
maxNum = 1

for i in range(1000001):
    currentCount = collatzRule(i)
    if maxCount < currentCount:
        maxCount = currentCount
        maxNum = i
        print(maxNum, maxCount)
print('计算结束')
