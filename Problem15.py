'''
网格路径
从一个2*2网格的左上角出发，若只允许向右或向下移动，则恰好有条6抵达右下角的路径。
对于20*20网格，这样的路径有多少条？
'''
'''
(自己的思路，但是时间复杂度太高了，n多个小时算不出来）
网格路径的遍历，20*20的网格共有21*21=441个点，从左上角(0,0)出发到达(20,20)
    思路如下：
    1.从第一个点开始，看其能否走两条路（向右或向下），如果可以，则将这个点放入堆
栈，并向右走，看下一个点是否能走两条，如果是也放入堆栈并向右走..路径上只能向下或
只能向右的点直接跳过看下一个点，直到到达右下角，路径计数+1。
    2.此时做出栈操作，出栈的点一定是这条路上最后一个拥有分叉的点，从这个点向下走
，继续重复1中的操作，到达右下角，路径计数+1。
    3.如此2->1->2->1...不断循环，直到堆栈为空。
'''

'''
(正确思路，动态规划）
我们利用2×2的格子中的3×3个顶点来计算到达每个顶点有多少条路径，我们初始化一个数
组3×3的数组x，其中每个值为0，之后会对其进行更新。

对于最上边一行和最左边一行的顶点来说，从起点开始向右或向下到达这些顶点的路径只有
一条，所以我们将x[0][0]，x[0][1]，x[0][2]，x[1][0]和x[2][0]都更新为1。

到达第二行的第二个顶点的路径数=（到达第二行第一个顶点的路径数+到达第一行第二个顶
点的路径数），因为只有第二行第一个顶点和第一行第二个顶点可以通过向右或者向下到达
该点，故到达每个顶点的路径数都由到它左边顶点的路径数和到它上边顶点的路径数相加得
到。

对于20×20的格子，用这样的解题思路就可以得到结果。
'''

def routes(n):
    x = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        x[0][i] = 1
        x[i][0] = 1
    for i in range(1, n + 1, 1):
        for j in range(1, n + 1, 1):
            x[i][j] = x[i - 1][j] + x[i][j - 1]
    return x[n][n]

print(routes(20))
