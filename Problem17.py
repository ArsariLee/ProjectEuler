'''
表达数字的英文字母计数
把1到5写成英文单词分别是：one、two、three、four、five。这些单词一共用了3+3+5+4
+4=19个字母。

如果把1到1000都写成英文单词，一共要用多少个字母？

注意： 不要算上空格和连字符。例如，342（three hundred and forty-two）包含个23字
母，而115（one hundred and fifteen）包含20个字母。单词“and”的使用方式遵循英式
英语的规则。
'''

# 特殊的 one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,
#        thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
#        twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety,hundred,thousand

# 创建一个生成数字单词的函数
def numberToWord(num):
    within19 = ['one','two','three','four','five','six','seven','eight','nine',\
                'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
                'seventeen','eighteen','nineteen']
    above20 = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    hundreds = num // 100
    num = num % 100
    # 十位个位的处理
    if 0 < num < 20:
        doubleDigit = within19[num - 1]
    elif num == 0:
        doubleDigit = ""
    elif num % 10 == 0:
        doubleDigit = above20[num // 10 - 2]
    else:
        doubleDigit = above20[num // 10 - 2] + within19[num % 10 - 1]
    # 百位千位的处理
    if hundreds == 0:
        hundredsDigit = ""
    elif hundreds == 10:
        hundredsDigit = "onethousand"
    elif num == 0:
        hundredsDigit = within19[hundreds - 1] + "hundred"
    else:
        hundredsDigit = within19[hundreds - 1] + "hundredand"
    return (hundredsDigit + doubleDigit)


strNum = ""
for i in range(1, 1001):
    # print(numberToWord(i))
    strNum += numberToWord(i)
print(len(strNum))


    
