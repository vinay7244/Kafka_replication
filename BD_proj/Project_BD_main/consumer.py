import socket
import threading
import time
def handle(p,t,ch):
    dic=[]
    c=socket.socket ()
    c.connect(('localhost',int(p)))
    if len(ch)>0:
        c.send(bytes("begin:"+t,'utf-8'))
    else:
        c.send(bytes(":"+t,'utf-8'))
    while True:
        st=c.recv(1024).decode()
        if len(st)>0:
            if st not in dic:
                print(st)
                dic.append(st)
                time.sleep(2)
        if st!="Acknowledged":
            time.sleep(2)
            cd=input("Would you wish to unsubscribe?")
            if cd=="yes":
                c.send(bytes("$$:$$",'utf-8'))
                break



def beg():
    while True:
            p=input("Enter the port number that you wish to join")
            t=input("Enter the topic name")
            ch=input("Do you want data from begining or no?")
            thread=threading.Thread(target=handle,args=(p,t,ch))
            thread.start()
            time.sleep(20)
beg()

























# p=input("Enter the port Number that you need to connect")
# c.connect ( ('localhost',int(p)))
# while True:
#     t=input("Enter topic name")
#     cho=input("Do you want data from begining or not")
#     if len(cho)>0:
#         c.send (bytes("begin:"+t, 'utf-8'))
#         st=c.recv (1024). decode()
#         if len(st)>0:
#             print(st)
#     else:
#         c.send(bytes(":"+t,'utf-8'))

#         st=c.recv (1024). decode()
#         if len(st)>0:
#             print(st)
#     b=input("Would you wish to unsubscribe?")
#     if b=="yes":
#         c.send(bytes("$$:$$",'utf-8'))
#         break
