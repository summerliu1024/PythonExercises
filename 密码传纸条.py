
"""
题目求的是字母位置，也就是 (下标 + 1)， 所以我们计算分组的下标和字母下标就好
开始需要计算 组的初始下标和字母在组中的初始下标，也就是字母的  (初始位置-1)，
"""
#初始字母
letterList = ['ABCDEFGHI','JKLMNOPQR','STUVWXYZ*']
#字母下标
letterSubDict = {}
#计算初始下标
def comp_sub():
    global letterSubDict
    for i,j in enumerate(letterList):
        for a,b in enumerate(j):
            letterSubDict[b] = [i,a]
 
# 这里获取时间和字符串，并计算字母移动过后的下标
def encry():
    global  letterSubDict
    date = input('输入日期:')
    dateList =  [int(i) for i in date.split(' ')]
    strInfor = input('输入字符串:')
    #将空格转为 * 号
    strInfor = strInfor.replace(' ','*')
    #月份实际移动次数和天数实际移动次数
    Mnums = (dateList[0]-1) % 3
    Dnums = (dateList[1]-1) % 9
    """
    。。。。。。。。。计算字母此时位置。。。。。。。。。。
    这里很神奇：
    Python序列中的一个值按题目的方法移动,移动次数不大于序列长度的话， 下标 - 移动距离 = 移动后结果的反向下标
    (序列长度 + 反向下标) % 序列长度 = 正向下标 
    正向下标 + 1 = 字母位置
    """
    for i,j in letterSubDict.items():
        j[0] = str((3+(j[0]-Mnums))%3+1)
        j[1] = str((9+(j[1]-Dnums))%9+1)
        letterSubDict[i] = j
    #此处遍历字符串，并从字典中把字母的位置取出来就好
    position = []
    for i in strInfor:
        posit = ''.join(letterSubDict[i])
        position.append(posit)
    position = ' '.join(position)
    print(position)
 
if __name__ == '__main__':
    comp_sub()
    encry()