'''
偶斐波那契数
斐波那契数列中的每一项都是前两项的和。由1和2开始生成的斐波那契数列的前10项为：
1,2,3,5,8,13,21,34,55,89...

考虑该斐波那契数列中不超过四百万的项，求其中为偶数的项之和。
'''

# a=1,b=2,轮流加和每一次的b并判断a.b是否大于四百万

a, b, c = 1, 2, 2

while 1:
    a = a + b
    if a > 4000000:
        break
    print(a)
    if a % 2 == 0:
        c = c + a
    
    b = b + a
    print(b)
    if b > 4000000:
        break
    if b % 2 == 0:
        c = b + c

print(a, b, c)
        