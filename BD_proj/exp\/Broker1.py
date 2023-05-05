import socket
import threading
s=socket.socket()
s.bind(('localhost',9998))
dic={}
def handle_broker(c,addr,str):
    a,b=str.split(":")
    a=a[1:]
    f=open(a,"a")
    f.write(str+'\n')
    f.close()

def handle_consumer(c,addr,str):
    a,b=str.split(":")
    sc=socket.socket()
    sc.connect(('localhost',9999))
    sc.send(bytes("*:"+b,'utf-8'))
    sc.close()



def beg():
    s.listen()
    while True:
        c,addr=s.accept()
        str=c.recv(1024).decode()
        a,b=str.split(':')
        if a!="begin" and len(a)!=0:
            if a[0]=="#":
                a=a[1:]
                thread=threading.Thread(target=handle_broker,args=(c,addr,str))
                thread.start()
            for k,v in dic.items():
                if v==a:
                    k.send(bytes(a+':'+b,'utf-8'))
        elif len(a)==0:
            dic[c]=b
            thread=threading.Thread(target=handle_consumer,args=(c,addr,str))
            thread.start()
beg()



