import socket
def sus():
    p=9997
    t=input("Enter your Topic name")
    c = socket.socket ()
    c.connect ( ('localhost',p))
    data = input("Enter topic data:")
    while True and data!="stop":
        c.send(bytes (t+':'+data, 'utf-8'))
        st=c.recv(1024).decode()
        if st=="Acknowledged":
            print(st)
            break
    c.close()
sus()