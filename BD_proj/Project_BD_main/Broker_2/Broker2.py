import socket
import threading
import os
s=socket.socket()
sub={}
s.bind(('localhost',9999))
def round_robin(c,st):
    st=st[1:]
    a,b=st.split(":")
    f=open(a,"a")
    f.write(st)
    f.write('\n')
    f.close()
def rep(c,st):
    ch=st[0]
    st=st[1:]
    a,b=st.split(":")
    f=open(ch+a,"a")
    f.write(st)
    f.write('\n')
    f.close()
def begin(c,b):
    p='/Users/apple/Desktop/Project_BD_main/Broker_2/'
    i=os.path.exists(p+b)
    if i:
        f=open(b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()
    i=os.path.exists(p+"0"+b)
    if i:
        f=open("0"+b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()
    i=os.path.exists(p+"1"+b)
    if i:
        f=open("1"+b,"r")
        for x in f:
            c.send(bytes(x,'utf-8'))
        f.close()
s.listen()
while True:
    c,addr=s.accept()
    st=c.recv(1024).decode()
    if len(st)>0:
        a,b=st.split(":")
        if a=="$$":
            del sub[c]
        elif len(a)!=0 and a!="begin":
            if st[0]=="2":
                thread=threading.Thread(target=round_robin,args=(c,st))
                thread.start()
            elif st[0]=="0" or st[0]=="1":
                thread=threading.Thread(target=rep,args=(c,st))
                thread.start()
            a=a[1:]
            st=st[1:]
            for k,v in sub.items():
                if v==a:
                    k.send(bytes(st,'utf-8'))
        elif len(a)==0:
            c.send(bytes("Acknowledged",'utf-8'))
            sub[c]=b
        elif a=="begin":
            c.send(bytes("Acknowledged",'utf-8'))
            sub[c]=b
            thread=threading.Thread(target=begin,args=(c,b))
            thread.start()
