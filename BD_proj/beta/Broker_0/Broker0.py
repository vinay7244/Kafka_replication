import socket
import threading
import os
dic={}
sub={}
s=socket.socket()
s.bind(('localhost',9997))
def Round_robin(c,str):
    a,b=str.split(":")
    f=open(a,"a")
    f.write(str)
    f.write('\n')
    f.close()
    b1=socket.socket()
    b1.connect(('localhost',9998))
    b1.send(bytes("0"+str,'utf-8'))
    b1.close()
    b2=socket.socket()
    b2.connect(('localhost',9999))
    b2.send(bytes("0"+str,'utf-8'))
    b2.close()
def rep(c,st,i):
    a,b=st.split(":")
    f=open(str(i)+a,"a")
    f.write(st)
    f.write('\n')
    f.close()
    b1=socket.socket()
    b1.connect(('localhost',9998))
    b1.send(bytes(str(i)+st,'utf-8'))
    b1.close()
    b2=socket.socket()
    b2.connect(('localhost',9999))
    b2.send(bytes(str(i)+st,'utf-8'))
    b2.close()
def begin(c,b):
    p='/Users/apple/Desktop/Project_BD-main/Broker_0/'
    i=os.path.exists(p+b)
    if i:
        f=open(b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()
    i=os.path.exists(p+"1"+b)
    if i:
        f=open("1"+b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()
    i=os.path.exists(p+"2"+b)
    if i:
        f=open("2"+b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()


def beg():
    s.listen()
    while True:
        c,addr=s.accept()
        str=c.recv(1024).decode()
        if len(str)>0:
            a,b=str.split(":")
            if a=="$$":
                del sub[c]
            elif len(a)!=0 and a!="begin":
                c.send(bytes("Acknowledged",'utf-8'))
                if a not in dic or dic[a]==0:
                    dic[a]=1
                    thread=threading.Thread(target=Round_robin,args=(c,str))
                    thread.start()
                elif dic[a]==1:
                    dic[a]=2
                    thread=threading.Thread(target=rep,args=(c,str,1))
                    thread.start()
                elif dic[a]==2:
                    dic[a]=0
                    thread=threading.Thread(target=rep,args=(c,str,2))
                    thread.start()
                for k,v in sub.items():
                    if v==a:
                        k.send(bytes(str,'utf-8'))
            elif len(a)==0:
                sub[c]=b
                c.send(bytes("Acknowledged",'utf-8'))
            elif a=="begin":
                sub[c]=b
                c.send(bytes("Acknowledged",'utf-8'))
                thread=threading.Thread(target=begin,args=(c,b))
                thread.start()


beg()

