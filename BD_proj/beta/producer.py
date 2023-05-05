import socket
import time
def sus():
    p=9997
    t=input("Enter your Topic name")
    c = socket.socket ()
    try:
        c.connect ( ('localhost',p))
    except:
        p=9998
        cc=socket.socket()
        cc.connect(('localhost',p))
        time.sleep(2)
    data = input("Enter topic data:")
    while True and data!="stop":
        if p==9997:
            c.send(bytes (t+':'+data, 'utf-8'))
            st=c.recv(1024).decode()
            c.close()
        else:
            cc.send(bytes("#"+t+":"+data,'utf-8'))
            st=cc.recv(1024).decode()
            cc.close()
        if st=="Acknowledged":
            print(st)
            break
sus()