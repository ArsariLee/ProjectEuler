'''
幂的数字和
2^15=32768，而32768的各位数字之和是3+2+7+6+8=26。

2^1000的各位数字之和是多少？
'''

a = 2 ** 1000
sumA = 0
a = str(a)
listA = []

for i in range(len(a)):
    listA.append(a[i])
print(listA)

for i in range(len(listA)):
    sumA += int(listA[i])
    print(sumA)
