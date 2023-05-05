import socket
import threading
import time
def handle(t,data):
        p=9997
        c = socket.socket ()
        c.connect ( ('localhost',p))
        c.send(bytes (t+':'+data, 'utf-8'))
        st=c.recv(1024).decode()
        if st=="Acknowledged":
            print(st+'\n')
        c.close()

def sus():
    while True:
        t=input("Enter your Topic name")
        data = input("Enter topic data:")
        thread=threading.Thread(target=handle,args=(t,data))
        thread.start()
        time.sleep(1)
        t=input("Would you wish to close\n")
        if t=="yes":
            break
sus()