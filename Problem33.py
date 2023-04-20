'''
消去数字的分数

49/98是一个有趣的分数，因为缺乏经验的数学家可能在约简时错误地认为，等式49/98 = 4
/8之所以成立，是因为在分数线上下同时抹除了9的缘故。

我们也会想到，存在诸如30/50 = 3/5这样的平凡解。

这类有趣的分数恰好有四个非平凡的例子，它们的分数值小于1，且分子和分母都是两位数。

将这四个分数的乘积写成最简分数，求此时分母的值。
'''

# (a*10+b)/(c*10+d)，ab和cd之间至少有两数相等，比较两分数是否相等，则是比较
# A的分子*B的分母是否等于A的分母*B的分子

a, b, c, d = 1, 1, 1, 1






productUp = 1
productDown = 1


for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            d = a
            upA = a * 10 + b
            downA = c * 10 + d
            if upA >= downA:
                continue
            if (upA * c) == (downA * b):
                productUp *= upA
                productDown *= downA
                print(a,b,"/",c,d)

        for c in range(1, 10):
            d = b
            upA = a * 10 + b
            downA = c * 10 + d
            if upA >= downA:
                continue
            if (upA * c) == (downA * a):
                productUp *= upA
                productDown *= downA
                print(a,b,"/",c,d)

        for d in range(1,10):
            c = a
            upA = a * 10 + b
            downA = c * 10 + d
            if upA >= downA:
                continue
            if upA * d == downA * b:
                productUp *= upA
                productDown *= downA
                print(a,b,"/",c,d)
                
        for d in range(1,10):
            c = b
            upA = a * 10 + b
            downA = c * 10 + d
            if upA >= downA:
                continue
            if upA * d == downA * a:
                productUp *= upA
                productDown *= downA
                print(a,b,"/",c,d) 
        

print(productUp, productDown)
                    
