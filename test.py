# # def test(x,l=[]):
# # #     for o in range(x):
# # #         l.append(o)
# # #
# # #     print(l)
# # #
# # # test(3)
# # # test(1,[3,2,1])
# # # test(3)
#
#
# # a = [1,3,5,7]
# # b = [1,3,4,6,8]
# # c = list(set(a) | set(b))
# #
# # print(c)
#
#
# import re
#
# a = """<a  href=" " data-hide=""><span class="surl-text">#我的逸件事#</span></a > 之训练其实真的是重复到无聊的事，所以一直没放出来<span class="url-icon">< img alt=[衰] src="//h5.sinaimg.cn/m/emoticon/icon/default/d_shuai-ade42a9895.png" style="width:1em; height:1em;" /></span><br /><a data-url="http://t.cn/E5ZJLL6" href="http://miaopai.com/show/lAcSXbh1DLPxwgHHukDnwmtr~-bmyfjhwoICHw__.htm?showurl=http%3A%2F%2Fmiaopai.com%2Fshow%2FlAcSXbh1DLPxwgHHukDnwmtr%7E-bmyfjhwoICHw__.htm&url_open_direct=1&toolbar_hidden=1&url_type=39&object_type=video&pos=1&containerid=23044201b08df7b0fa9c49db35027981ffc043&luicode=10000011&lfid=1076035781311106" data-hide=""><span class='url-icon'>< img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_video_default.png'></span><span class="surl-text">敖子逸_的秒拍视频</span></a ><br /><a data-url="http://t.cn/E5ZJLL9" href="http://miaopai.com/show/nUKsnfSw-q75WK~DvPyowC0b4DQM7jCaCDibxw__.htm?showurl=http%3A%2F%2Fmiaopai.com%2Fshow%2FnUKsnfSw-q75WK%7EDvPyowC0b4DQM7jCaCDibxw__.htm&url_open_direct=1&toolbar_hidden=1&url_type=39&object_type=video&pos=1&containerid=2304427feaf64672290da49790b1498174b45c&luicode=10000011&lfid=1076035781311106" data-hide=""><span class='url-icon'>< img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_video_default.png'></span><span class="surl-text">敖子逸_的秒拍视频</span></a >"""
#
# b=re.findall(r"[\u4e00-\u9fa5]",a)
#
# print(b)

# import re
#
# str = """/\sd中@国%￥测试……&*结哈、‘、‘’’哈国际SJGKLJGJ化可脚后跟123"""
#
# res = re.findall(r'\w',str)
# print(res)

# from selenium import webdriver
#
# import time
#
#
# driver = webdriver.Chrome()
# driver.get("http://mail.163.com/")
# time.sleep(5)
#
# iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# driver.switch_to.frame(iframe)
# # 用户名 密码
# elem_user = driver.find_element_by_name("email")
# elem_user.send_keys("xxxx")
# elem_pwd = driver.find_element_by_name("password")
# elem_pwd.send_keys("XXXXXX")
# elem_but = driver.find_element_by_id("dologin")
#
# elem_but.click()
# time.sleep(5)
# driver.close()
# driver.quit()

# a=[i**i for i in range(3)]
# print(a)
#
# print('a'<'b'<'c')
#
#
# a='a'
# print(a>'b' or 'c')
# import re
#
#
# def fun(temp):
#     ret = temp.group()
#     l = []
#     for s in ret:
#         l.append(s)
#
#     l.reverse()
#     str = ''
#     for s in l:
#         str += s
#
#     return str
#
#
# # str1 = 'abc-1de/fg'
# str1 = '1233aasxcd/-1w12=sdeer'
# ret = re.sub(r'([a-zA-Z]+)', fun, str1)
#
# print(ret)

# a = [1, 2,4,2,4,5,7,10,5,5,7,8,9,0,3]
# # a.sort()
# # last = a[-1]
# # for i in range(len(a)-2, -1, -1):
# #     if last == a[i]:
# #         del a[i]
# #     else:
# #         last = a[i]
# # print(a)
# #
# #
# # c=[i*2 for i in [1,2,3]]
# # print(c)
#
# a=[{1:'a'},{2:'b'}]
# m_list=list()
#
# for i in a:
#     for key,value in i.items():
#         m_list.append({'value':value,'key':key})
#
#
# print(m_list)
#
#
#
# num=9
# def f1():
#     num=20
#
# def f2():
#     print(num)
#
# f2()
# f1()
# f2()

# a=[[1,2],[3,4],[5,6]]
# c=list()
# for i in a:
#     for var in i:
#         c.append(var)
#
# print(c)
# # def test(x,l=[]):
# # #     for o in range(x):
# # #         l.append(o)
# # #
# # #     print(l)
# # #
# # # test(3)
# # # test(1,[3,2,1])
# # # test(3)
#
#
# # a = [1,3,5,7]
# # b = [1,3,4,6,8]
# # c = list(set(a) | set(b))
# #
# # print(c)
#
#
# import re
#
# a = """<a  href=" " data-hide=""><span class="surl-text">#我的逸件事#</span></a > 之训练其实真的是重复到无聊的事，所以一直没放出来<span class="url-icon">< img alt=[衰] src="//h5.sinaimg.cn/m/emoticon/icon/default/d_shuai-ade42a9895.png" style="width:1em; height:1em;" /></span><br /><a data-url="http://t.cn/E5ZJLL6" href="http://miaopai.com/show/lAcSXbh1DLPxwgHHukDnwmtr~-bmyfjhwoICHw__.htm?showurl=http%3A%2F%2Fmiaopai.com%2Fshow%2FlAcSXbh1DLPxwgHHukDnwmtr%7E-bmyfjhwoICHw__.htm&url_open_direct=1&toolbar_hidden=1&url_type=39&object_type=video&pos=1&containerid=23044201b08df7b0fa9c49db35027981ffc043&luicode=10000011&lfid=1076035781311106" data-hide=""><span class='url-icon'>< img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_video_default.png'></span><span class="surl-text">敖子逸_的秒拍视频</span></a ><br /><a data-url="http://t.cn/E5ZJLL9" href="http://miaopai.com/show/nUKsnfSw-q75WK~DvPyowC0b4DQM7jCaCDibxw__.htm?showurl=http%3A%2F%2Fmiaopai.com%2Fshow%2FnUKsnfSw-q75WK%7EDvPyowC0b4DQM7jCaCDibxw__.htm&url_open_direct=1&toolbar_hidden=1&url_type=39&object_type=video&pos=1&containerid=2304427feaf64672290da49790b1498174b45c&luicode=10000011&lfid=1076035781311106" data-hide=""><span class='url-icon'>< img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_video_default.png'></span><span class="surl-text">敖子逸_的秒拍视频</span></a >"""
#
# b=re.findall(r"[\u4e00-\u9fa5]",a)
#
# print(b)

# import re
#
# str = """/\sd中@国%￥测试……&*结哈、‘、‘’’哈国际SJGKLJGJ化可脚后跟123"""
#
# res = re.findall(r'\w',str)
# print(res)

# from selenium import webdriver
#
# import time
#
#
# driver = webdriver.Chrome()
# driver.get("http://mail.163.com/")
# time.sleep(5)
#
# iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# driver.switch_to.frame(iframe)
# # 用户名 密码
# elem_user = driver.find_element_by_name("email")
# elem_user.send_keys("xxxx")
# elem_pwd = driver.find_element_by_name("password")
# elem_pwd.send_keys("XXXXXX")
# elem_but = driver.find_element_by_id("dologin")
#
# elem_but.click()
# time.sleep(5)
# driver.close()
# driver.quit()

# a=[i**i for i in range(3)]
# print(a)
#
# print('a'<'b'<'c')
#
#
# a='a'
# print(a>'b' or 'c')
# import re
#
#
# def fun(temp):
#     ret = temp.group()
#     l = []
#     for s in ret:
#         l.append(s)
#
#     l.reverse()
#     str = ''
#     for s in l:
#         str += s
#
#     return str
#
#
# # str1 = 'abc-1de/fg'
# str1 = '1233aasxcd/-1w12=sdeer'
# ret = re.sub(r'([a-zA-Z]+)', fun, str1)
#
# print(ret)

# a = [1, 2,4,2,4,5,7,10,5,5,7,8,9,0,3]
# # a.sort()
# # last = a[-1]
# # for i in range(len(a)-2, -1, -1):
# #     if last == a[i]:
# #         del a[i]
# #     else:
# #         last = a[i]
# # print(a)
# #
# #
# # c=[i*2 for i in [1,2,3]]
# # print(c)
#
# a=[{1:'a'},{2:'b'}]
# m_list=list()
#
# for i in a:
#     for key,value in i.items():
#         m_list.append({'value':value,'key':key})
#
#
# print(m_list)
#
#
#
# num=9
# def f1():
#     num=20
#
# def f2():
#     print(num)
#
# f2()
# f1()
# f2()

# a=[[1,2],[3,4],[5,6]]
# c=list()
# for i in a:
#     for var in i:
#         c.append(var)
#
# print(c)


# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
#
# f(2)
# f(3,[3,2,1])
# f(3)
#
# def add(a):
#     a+=a
#
# a=1
#
# add(a)
#
# print(a)
#
# a=[1,2,3]
# add(a)
# print(a)

#
# a=[1,2,3,4,5,6]
# b=[3,6]
# c=list()
#
# for i in a:
#     if i not in b:
#         c.append(i)
#
# print(c)
#
# str1='a bb    ccc'
#
# str2=str1.split()
# print(str2)
# str2="-".join(str2)
# print(str2)


# class Parent(object):
#     x=1
# class C1(Parent):
#     pass
# class C2(Parent):
#     pass
#
# print(Parent.x,C1.x,C2.x)
#
#
# C1.x=2
#
# print(Parent.x,C1.x,C2.x)
#
# Parent.x=3
#
# print(Parent.x,C1.x,C2.x)
# import keyword
#
# str1 = input("请输入：")
# print(keyword.iskeyword(str1))
# import random
# test1 = (1,2,3,4,5,6,7,8,9,0,)
# test2 = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',)
# num1 = random.sample(test1,2)
# nump1 = random.sample(test2,2)
# test_out = random.sample(num1 + nump1,4)
# test_print = str(test_out[0]) + str(test_out[1]) + str(test_out[2]) + str(test_out[3])
# print(test_print)
#
# # 求1-2+3-4+5...99的所有数的和
# n = 1
# s = 0  # s是之前所有数的总和
# while n < 100:
#     temp = n % 2
#     if temp == 0:
#         s = s - n
#     else:
#         s = s + n
#     n = n + 1
#
# print(s)

# def dprint(char):
#     def print_sty(func):
#         def inner():
#             print(char*15)
#             func()
#             print(char*15)
#         return inner
#     return print_sty
#
#
# @dprint("=")
# @dprint("*")
# def myprint():
#     print("python decorator")
#
#
#
# myprint()

# n1=123
# n2=123
#
# print(id(n1))
# print(id(n2))
#

# import sys
# d={}
# for i in range(26):
#     d[chr(i+ord("a"))]=chr((i+13)%26+ord("a"))
#
# for c in "Python":
#     sys.stdout.write(d.get(c,c))
#
# x=11
# def double(x):
#     x+=x
#     print(x)
#
#
# double(x)
#
# dict={"a":1,"b":2,"b":3}
#
# print(dict['b'],(dict['a'],dict['b']))

# print([i*i for i in xrange(3)])

# class A():
#     pass
#
# a1=A()
# a2=A()
# print(a1 is a2)
# print(a1==a2)



# print(c)
from PIL import ImageGrab

# 参数说明
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
try:
    x = int(input("请输入横坐标："))
    y = int(input("请输入纵坐标："))
    w = int(input("请输入长坐标："))
    h = int(input("请输入高坐标："))
    bbox = (x, y, x+w, y+h)
    im = ImageGrab.grab(bbox)

    # 参数 保存截图文件的路径
    im.save('as.png')

    z1 = (x, y)
    z2 = (x + w, y)
    z3 = (x, y + h)
    z4 = (x + h, y + w)

    print("截取区域的坐标为:{},{},{},{}".format(z1, z2, z3, z4))

except Exception as e:
    print(e)

