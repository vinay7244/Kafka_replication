import os
f=open("sathya.txt","a")
f.write("hi")
f.close()
i=os.path.exists("/Users/apple/Desktop/Project_BD-main/Broker_0/sathya")
print(i)