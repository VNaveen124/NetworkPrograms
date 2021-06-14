#client1.py
import socket

s=socket.socket()
s.connect(("localhost",8989) )
print("---------------------------------------------------")
print("Client Side Program connected to server side program");
print("---------------------------------------------------")
cdata=input("Enter a Message:")
s.send(cdata.encode())
print("---------------------------------------------------")
sdata=s.recv(1024).decode()
print("Data from Server at Client side={}".format(sdata))
print("---------------------------------------------------")
