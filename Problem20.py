'''
阶乘数字和
n!的意思是n*(n-1)*...*1。
例如，10!=10*9*8*7*...*3*2*1=3628800，所以10!的各位数字和是3+6+2+8+8+0+0=27。
求100!的各位数字和。
'''
# 没难度

product = 1
for i in range(1, 101):
    product *= i
product = str(product)

sumProduct = 0

for i in range(len(product)):
    sumProduct += int(product[i])

print(sumProduct)
