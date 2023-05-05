import socket
c = socket.socket ()
p=input("Enter the port Number that you need to connect")
c.connect ( ('localhost',int(p)))
t=input("Enter topic name")
cho=input("Do you want data from begining or not")
if len(cho)>0:
    c.send (bytes("begin:"+t, 'utf-8'))
    while True:
        st=c.recv (1024). decode()
        if len(st)>0:
            print(st)
else:
    c.send(bytes(":"+t,'utf-8'))
    while True:
        st=c.recv (1024). decode()
        if len(st)>0:
            print(st)
        if st!="Acknowledged":
            b=input("Would you wish to unsubscribe?")
            if b=="yes":
                c.send(bytes("$$:$$",'utf-8'))
                break
