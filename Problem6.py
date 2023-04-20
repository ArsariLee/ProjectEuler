'''
平方的和与和的平方之差
前十个自然数的平方的和是385
前十个自然数的和的平方是3025
因此，前十个数的平方的和与和的平方之差是2640。
求前一百个数的平方的和与和的平方之差。
'''

# 直接算,没什么技术含量
squareSum, sumSquare = 0, 0

for i in range(1, 101):
    squareSum += i * i
print(squareSum)

for i in range(1, 101):
    sumSquare += i
sumSquare **= 2
print(sumSquare)

print(abs(squareSum - sumSquare))
