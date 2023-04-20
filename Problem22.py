'''
名字打分
在文本文件names.txt（右击并选择“目标另存为……”）中包含了五千多个名字。首先将
它们按照字母序排列，然后计算出每个名字的字母价值，乘以它在按字母顺序排列后的位
置，就算出了这个名字的得分。

例如，按照字母序排列后，位于第938位的名字是COLIN，它的字母价值是3+15+12+9+14=53
。因此，COLIN这个名字的得分是938*53=49714。

上述文本文件中，所有名字的得分之和是多少？
'''

file = open("p022_names.txt")
# 读取文本并分隔然后存入列表，去除各个名字首尾引号
fileList = file.read().split(",")

for i in range(len(fileList)):
    fileList[i] = fileList[i].strip('"')

fileList.sort()

fileValueList = []

# ASCII码A是65，所以字母价值要-64

for i in range(len(fileList)):
    sum1 = 0
    for j in range(len(fileList[i])):
        sum1 += (ord(fileList[i][j]) - 64)
    fileValueList.append(sum1 * (i + 1))

print(sum(fileValueList))

