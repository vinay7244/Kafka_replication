import socket
import threading
s=socket.socket()
s.bind(('localhost',9999))
dic={}
l1=[]
l2=[]
d={}
def handle_consumer(c,addr,a,b):
    f=open(b,"r")
    for x in f:
        c.send(bytes(x,'utf-8'))

def handle_producer(c,addr,a,b):
    f=open(a,"a")
    f.write(a+":"+b+'\n')
    f.close()
    sc=socket.socket()
    sc.connect(('localhost',9998))
    sc.send(bytes("#"+str+"0",'utf-8'))
    sc.close()

def handle_broker(str,i):
    a,b=str.split(":")
    if i==1:
        f=open(a+"1","a")
    else:
        f=open(a+"2","a")
    f.close()


    sc=socket.socket()
    if i==1:
        sc.connect(('localhost',9998))
        sc.send(bytes("#"+str+"1",'utf-8'))
    else:
        sc.connect(('localhost',9997))
        sc.send(bytes("#"+str+"2",'utf-8'))
    sc.close()



def beg():
    s.listen()
    while True:
        c,addr=s.accept()
        str=c.recv(1024).decode()
        a,b=str.split(':')
        if a=="begin":
            thread=threading.Thread(target=handle_consumer,args=(c,addr,a,b))
            thread.start()
            dic[c]=b
        elif len(a)==1 or len(a)==0:
            print(c)
            print(b)
            print("IN len=0")
            if len(a)==1 and a=="*":
                if a not in l1:
                    l1.append(b)
            elif len(a)==1 and a=="$":
                if a not in l2:
                    l2.append(b)
            else:
                dic[c]=b
            
        else:
            if a not in d or d[a]==0:
                d[a]=1
                thread=threading.Thread(target=handle_producer,args=(c,addr,a,b))
                thread.start()
            elif d[a]==1:
                d[a]=2
                thread=threading.Thread(target=handle_broker,args=(str,1))
                thread.start()
            elif d[a]==2:
                d[a]=0
                thread=threading.Thread(target=handle_broker,args=(str,2))
                thread.start()
            for k,v in dic.items():
                if v==a:
                    sd=a+':'+b
                    k.send(bytes(sd,'utf-8'))
            for i in l1:
                if a==i:
                    scc=socket.socket()
                    scc.connect(('localhost',9998))
                    scc.send(bytes(str,'utf-8'))
                    scc.close()
            for i in l2:
                if a==i:
                    sdd=socket.socket()
                    sdd.connect(('localhost',9997))
                    sdd.send(bytes(str,'utf-8'))
                    sdd.close()
                
beg() 
