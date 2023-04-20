'''
Problem 1
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

# 0~1000之间循环求3和5的倍数，每次+1<1000就加，最后统计

a, b, c, d, e, f = 0, 0, 1, 1, 0, 1

while 1:
    if c * 3 >= 1000:
        break
    a = a + (c * 3)
    c = c + 1

while 1:
    if d * 5 >= 1000:
        break
    b = b + (d * 5)
    d = d + 1

while 1:
    if f * 15 >= 1000:
        break
    e = e + (f * 15)
    f = f + 1
print(a/3, b/5, e/15)
print(a, b, e)
print(a + b - e)

# 答案是233168
