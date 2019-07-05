# # # # # # # class Solution(object):
# # # # # # #     def isValid(self, s):
# # # # # # #
# # # # # # #         if len(s)<2 or len(s)%2!=0:
# # # # # # #             if s=='':
# # # # # # #                 return True
# # # # # # #             else:
# # # # # # #                 return False
# # # # # # #         count = 0
# # # # # # #         length = len(s)
# # # # # # #         # 将其中的(){}[] 都换掉，然后判断是否有剩余
# # # # # # #         while(count<length/2):
# # # # # # #             s = s.replace("{}","").replace("[]","").replace("()","")
# # # # # # #             count+=1
# # # # # # #         if len(s)>0:
# # # # # # #             return False
# # # # # # #         else:
# # # # # # #             return True
# # # # # # #
# # # # # # #
# # # # # # # my_str=input("请输入：")
# # # # # # # s=Solution()
# # # # # # # print(s.isValid(my_str))
# # # # # #
# # # # # #
# # # # # # class Minstack(object):
# # # # # #     def init(self):
# # # # # #         self.stack = []
# # # # # #         self.Minstack = []
# # # # # #     def isEmpty(self):
# # # # # #         return len(self.stack)<1
# # # # # #     def push(self,item):
# # # # # #         self.stack.append(item)
# # # # # #         if self.Minstack == [] or item<self.Minstack[-1]:
# # # # # #             self.Minstack.append(item)
# # # # # #     def top(self):
# # # # # #         if not self.isEmpty():
# # # # # #             return self.stack[-1]
# # # # # #     def getMin(self):
# # # # # #         if not self.isEmpty():
# # # # # #             return self.Minstack[-1]
# # # # # #     def pop(self):
# # # # # #         if not self.isEmpty():
# # # # # #             if self.Minstack[-1]==self.top():
# # # # # #                 self.Minstack.pop()
# # # # # #             self.stack.pop()
# # # # # # stack = Minstack()
# # # # # # stack.push(-2)
# # # # # # stack.push(0)
# # # # # # stack.push(-3)
# # # # # # stack.push(5)
# # # # # # stack.push(-4)
# # # # # # print(stack.getMin())
# # # # # # stack.pop()
# # # # # # print(stack.top())
# # # # # # print(stack.getMin())
# # # # # #
# # # # # #
# # # # #
# # # # # # while True:
# # # # # # #     pass
# # # # # # # x=1
# # # # # # # y=2
# # # # # # # main=x>y?x:
# # # # # #
# # # # # # class A():
# # # # # #     pass
# # # # # #
# # # # # # class B(A):
# # # # # #     pass
# # # # # # b=B()
# # # # # #
# # # # # # # print(issubclass(b,B))
# # # # # # print(issubclass(B,A))
# # # # # # print(isinstance(b,object))
# # # # # # print(isinstance(b,A))
# # # # #
# # # # # # def my(*args,a=1):
# # # # # #     pass
# # # # #
# # # # # # lis1=[n for n in range(1,5)]
# # # # # # print(lis1[5:])
# # # # # #
# # # # # # aa=[1,2,3]
# # # # # # aa.append([2,3,4,5])
# # # # # # print(len(aa))
# # # # #
# # # # # (s, x, f) = "no1"
# # # # #
# # # # # # s = x = f = '1'
# # # # # s,x,f='1'
# # # # # print(x,f,s)
# # # # #
# # # # #
# # # #
# # # # #
# # # # # class A():
# # # # #     def _do(self):
# # # # #         pass
# # # # #     def __do(self):
# # # # #         pass
# # # # #     def __do__(self):
# # # # #         pass
# # # # #
# # # # #     @property
# # # # #     def fool(self):
# # # # #         pass
# # # # #
# # # # # class B(A):
# # # # #     pass
# # # # #
# # # # # B().fool
# # # # # # B.__do__()
# # # # # # B._do()
# # # # # B.__do()
# # # # #
# # # # # x=sum(n for n in range(1,100,4))/2
# # # # # print(x)
# # # #
# # # # import re
# # # #
# # # # r=re.findall('(a|b)*c+[^0-9]]','abac10')
# # # # print(r)
# # #
# # #
# # # # my_num=[9,7,98,25,46,75]
# # # # print(sorted(my_num))
# # #
# # # # a={"x":1,"z":3}
# # # # b={"y":2,"z":4}
# # # #
# # # #
# # # # a.update(b)
# # # # print(a)
# # # #
# # # # # #
# # # # # # str1="spam and eggs"
# # # # # # # #
# # # # # # # # print(str1.startswith(str1[:len(str1)-
# # #
# # #
# # # # def num():
# # # # #     return [lambda x:x*i for i in range(4)]
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # print([m(8) for m in num()])
# # #
# # # a=[1,4,9,16,25,36,49,64,81,100]
# # #
# # # b=[i*i for i in range(1,11)]
# # # print(b)
# # #
# # # a = [1,2,3]
# # # b = [(1),(2),(3) ]
# # # c = [(1,),(2,),(3,) ]
# # #
# # # print(a)
# # # print(b)
# # # print(c)
# # # colors=['balck',"white"]
# # # sizes=["S","M","L"]
# # #
# # # a=[(color,size) for size in sizes for color in colors ]
# # #
# # # print(a)
# # #
# # class PC:
# #     def __init__(self,brand,price):
# #         self.brand = brand
# #         self.price = price
# #
# #     def play_movie(self):
# #         if self.brand == "联想":
# #             print("葫芦娃")
# #         else:
# #             print("葫芦娃")
# #     def sale_price(self):
# #             print("%s品牌电脑售价为%d" % (self.brand,self.price))
# #
# # lianxiang = PC("联想",5000)
# # mac = PC("苹果",10000)
# #
# # lianxiang.play_movie()
# # mac.play_movie()
# #
# # lianxiang.sale_price()
# import socket, time
#
# def header():
#     """describe what this function does
#         #you will see a hello page and with information about how to
#         use this system
#         #you can input the number you see to select what you want to do"""
#     print("*" * 50)
#     print("欢迎使用文件传输系统".center(40))
#     print("请选择您要进行的操作代码：\n1.服务器下载\n2.服务器上传\n3.退出系统")
#
# def download_file(tcpOrder_socket):
#     """describe what this function does
#         #this is a function that you can input your order to the server
#         and then you will download the file that you want to your PC
#          if the server does have the file that you want,it will tell you this information
#          also, you can download times before you quit this """
#     tcpOrder_socket.send(choice_num.encode("utf-8"))  # 给服务器下命令
#
#     while True:
#         #睡眠1s 防止频繁请求带来异常
#         time.sleep(1)
#         # 获取要发送的信息
#         file_name = input("请输入你要查找的文件名：")
#         # 准备发送内容至服务器
#         #time.sleep(1)
#         tcpOrder_socket.send(file_name.encode("utf-8"))
#         # 接收服务器反馈信息并限制字节数为1024
#         recv_msg = tcpOrder_socket.recv(1024)
#
#         # 此处需要标识唯一的字符去判断服务器有没有找到目标文件
#         if recv_msg.decode("utf-8") == "No such file or directory":
#             print("文件不存在")
#             continue
#         else:  # 如果收到了数据
#             print(recv_msg.decode("utf-8"))
#             print("downloading。。。。")
#             # 更换电脑后需要更改地址
#             with open(r"/Users/summer/Desktop/test/%s" % file_name, "wb") as dowanload_file:
#                 dowanload_file.write(recv_msg)  # 覆盖写入
#                 print("download complete!")
#                 ask_again = input("是否继续下载？1/继续 0/退出")
#
#         if ask_again == "1":
#             tcpOrder_socket.send(ask_again.encode("utf-8"))
#
#             continue
#         elif ask_again == "0":
#             # 向服务器发送本次下载停止命令
#             tcpOrder_socket.send(ask_again.encode("utf-8"))
#             tcpOrder_socket.close()
#             break
#
#
#
# def update_file(tcpOrder_socket):
#     """describe what this function does
#         #this is a function that you can update your file to the server
#         and the server will save the file at the right path
#         also you can update times before you quit"""
#     tcpOrder_socket.send(choice_num.encode("utf-8"))
#     while True:
#
#         updateFile_name = input("请输入你要上传的文件名")
#         # tcpOrder_socket.send(updateFile_name.encode("utf-8"))
#         # time.sleep(1)
#         print("本地搜索中")
#         # 捕捉异常  打开目标文件
#         try:
#             file_content = ""
#             # 更换电脑后需要更改地址
#             souce_file = open(r"/Users/summer/Desktop/test/%s" % updateFile_name, "r")
#
#             tcpOrder_socket.send(updateFile_name.encode("utf-8"))
#             time.sleep(1)
#             file_content = souce_file.read()
#
#         except Exception as fault_info:
#             # print(fault_info)
#             print("文件不存在")
#             # 此处需要给服务器发送文件不存在命令
#             # tcpOrder_socket.send("No such file or directory".encode("utf-8"))
#
#             continue
#         if not updateFile_name:
#             continue
#             # tcpOrder_socket.close()
#         elif file_content:
#             # 将内容发送给客户端
#             tcpOrder_socket.send(file_content.encode("utf-8"))
#             print("上传完成！")
#             # 再次接收客户端命令
#             ask_again = input("是否继续上传？1/继续 0/退出")
#         if ask_again == "0":
#             # 向服务器发送本次下载停止命令
#             tcpOrder_socket.send(ask_again.encode("utf-8"))
#             tcpOrder_socket.close()
#             break
#         else:
#             # 即使命令出错也当作再次进行上传任务
#             tcpOrder_socket.send("1".encode("utf-8"))
#             continue
#
#             # tcpOrder_socket.close()
#
#
#
# server_ip=""
# server_port=""
#
# while True:
#     server_ip = input("请输入服务器IP：")
#     server_port = input("请输入服务器Port：")
#     while True:
#         header()
#         # 创建套接字对象
#         try:# 抓取OSError: [Errno 99] Cannot assign requested address  异常
#             tcpOrder_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             #强制允许端口复用
#             tcpOrder_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#             locall_addr = ("", 7890)
#             # 绑定本地信息
#             tcpOrder_socket.bind(locall_addr)
#             #print(tcpOrder_socket)
#             tcpOrder_socket.connect((server_ip, int(server_port)))
#             choice_num = input("请输入操作代码：")
#         except Exception as link_fault:
#             # continue
#             print(link_fault)
#         #下载模式
#         if choice_num == "1":
#
#             #调用下载函数
#             download_file(tcpOrder_socket)
#             """following code is no longer used since there is a better way """
#             # tcpOrder_socket.send(choice_num.encode("utf-8"))  # 给服务器下命令
#             #
#             # while True:
#             #     time.sleep(1)
#             #     # 获取要发送的信息
#             #     file_name = input("请输入你要查找的文件名：")
#             #     # 准备发送内容至服务器
#             #     time.sleep(1)
#             #     tcpOrder_socket.send(file_name.encode("utf-8"))
#             #     # 接收服务器反馈信息并限制字节数为1024
#             #     recv_msg = tcpOrder_socket.recv(1024)
#             #     #此处需要标识唯一的字符去判断服务器有没有找到目标文件
#             #     if recv_msg.decode("utf-8")=="No such file or directory":
#             #         print("文件不存在")
#             #         continue
#             #     else:  # 如果收到了数据
#             #         print(recv_msg.decode("utf-8"))
#             #         print("downloading。。。。")
#             #         #更换电脑后需要更改地址
#             #         with open(r"/home/itcast/Desktop/summer/%s" % file_name, "wb") as dowanload_file:
#             #             dowanload_file.write(recv_msg)  # 覆盖写入
#             #             print("download complete!")
#             #             ask_again = input("是否继续下载？1/继续 0/退出")
#             #
#             #
#             #     if ask_again == "1":
#             #         tcpOrder_socket.send(ask_again.encode("utf-8"))
#             #
#             #         continue
#             #     elif ask_again == "0":
#             #         #向服务器发送本次下载停止命令
#             #         tcpOrder_socket.send(ask_again.encode("utf-8"))
#             #         tcpOrder_socket.close()
#             #         break
#             #
#             #         # tcpClient_socket.close()
#
#
#         #上传模式
#         elif choice_num == "2":
#             #调用上传函数
#             update_file(tcpOrder_socket)
#             """following code is no longer used since there is a better way """
#         #     tcpOrder_socket.send(choice_num.encode("utf-8"))
#         #     while True:
#         #
#         #         updateFile_name=input("请输入你要上传的文件名")
#         #         # tcpOrder_socket.send(updateFile_name.encode("utf-8"))
#         #         # time.sleep(1)
#         #         print("本地搜索中")
#         #         #捕捉异常  打开目标文件
#         #         try:
#         #             file_content=""
#         #             #更换电脑后需要更改地址
#         #             souce_file = open(r"/home/itcast/Desktop/summer/%s" % updateFile_name, "r")
#         #
#         #             tcpOrder_socket.send(updateFile_name.encode("utf-8"))
#         #             time.sleep(1)
#         #             file_content=souce_file.read()
#         #
#         #         except Exception as fault_info:
#         #             #print(fault_info)
#         #             print("文件不存在")
#         #             #此处需要给服务器发送文件不存在命令
#         #             #tcpOrder_socket.send("No such file or directory".encode("utf-8"))
#         #
#         #             continue
#         #         if not updateFile_name:
#         #             continue
#         #             #tcpOrder_socket.close()
#         #         elif file_content:
#         #             # 将内容发送给客户端
#         #             tcpOrder_socket.send(file_content.encode("utf-8"))
#         #             print("上传完成！")
#         #             # 再次接收客户端命令
#         #             ask_again = input("是否继续上传？1/继续 0/退出")
#         #         if ask_again == "0":
#         #             # 向服务器发送本次下载停止命令
#         #             tcpOrder_socket.send(ask_again.encode("utf-8"))
#         #             tcpOrder_socket.close()
#         #             break
#         #         else:
#         #             #即使命令出错也当作再次进行上传任务
#         #             tcpOrder_socket.send("1".encode("utf-8"))
#         #             continue
#         #
#         #         #tcpOrder_socket.close()
#         #
#         elif choice_num == "3":
#             print("system quit!")
#             tcpOrder_socket.close()
#             break
#         else:
#             print("请输入正确操作代码")
#
#
#
import os
import time

def main():
    content = '曹查理的python面试集-基础篇'
    while True:
        # 清理屏幕上的输出
        os.system('clear')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
