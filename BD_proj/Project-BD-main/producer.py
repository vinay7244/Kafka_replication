import socket
def sus():
    p=input("Enter port number of leader")
    t=input("Enter your Topic name")
    c = socket.socket ()
    try:
        c.connect ( ('localhost',int(p)))
    except:
        cc=socket.socket()
        p="9998"
        cc.connect(('localhost',9998))
    data = input("Enter topic data:")
    while True and data!="stop":
        if p=="9997":
            c.send(bytes (t+':'+data, 'utf-8'))
            st=c.recv(1024).decode()
        else:
            cc.send(bytes(t+':'+data,'utf-8'))
            st=cc.recv(1024).decode()
        if st=="Acknowledged":
            print(st)
            break
    c.close()
sus()