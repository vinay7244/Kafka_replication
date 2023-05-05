# import socket
# import subprocess
# import sys
# from datetime import datetime
# import random

# subprocess.call('clear', shell=True)

# remoteServer    = input("Enter a remote host to scan: ")
# remoteServerIP  = socket.gethostbyname(remoteServer)

# print("-" * 60)
# print("Please wait, scanning remote host", remoteServerIP)
# print("-" * 60)


# try:
#     kafkaports = []
#     leader = kafkaports[0]
#     for port in kafkaports:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         result = sock.connect_ex((remoteServerIP, port))
#         if result == 0:
#             print("Port {}: 	Open".format(port))
#         else:
#             if port == leader:
#                 leader = random.choice(list(set(kafkaports) - set(port)))
#                 print("Newly elected leader = {}\n".format(leader))
                
#             #restart the port
#             clientSocket = socket.socket()  
#             clientSocket.connect((remoteServerIP, port))  
#             print( "Node at port {} restarted successfully!".format(port))
#         sock.close()

# except KeyboardInterrupt:
#     print("Bye")
#     sys.exit()

# except socket.gaierror:
#     print('Hostname could not be resolved. Exiting')
#     sys.exit()

# except socket.error:
#     print("Couldn't connect to server")
#     sys.exit()

import socket
import subprocess
import sys
import os
import random
import time

subprocess.call('clear', shell=True)

print("-" * 60)
print("Please wait, scanning remote host 127.0.0.1")
print("-" * 60)


def zoo():
    try:
        baseport = 9997
        leader = baseport
        port = 9997
        brokerports = []
        count = 0

        # How many broker nodes are there initially
        while port <= 9999:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('localhost', port))
            if result == 1:
                print(1)
                break
            else:
                print(0)
                count += 1
                brokerports.append(port)
                port += 1
            sock.close()
        print(brokerports)
        print(port)

        while True:
            for p in brokerports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('localhost', p))
                if result == 0:
                    print("Port {}: 	Open".format(p))
                else:
                    print("Port {}: 	Close".format(p))

                    if p == leader:
                        brokerports.remove(p)
                        leader = random.choice(brokerports)
                        brokerports.append(p)
                        print("Newly elected leader = {}\n".format(leader))
                        
                    
                    #restart the port
                    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    clientSocket.bind(('127.0.0.1', p))
                    clientSocket.listen()
                    print( "Node at port {} restarted successfully!".format(p))

                sock.close()
            time.sleep(5)

    except KeyboardInterrupt:
        print("Bye")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

zoo()
