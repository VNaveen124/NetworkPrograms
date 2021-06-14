#client2.py----> This program accept a number from kbd at client, send to server and get its  square.
import socket
s=socket.socket()
s.connect(("localhost",9999) )
print("---------------------------------------------------")
print("Client Side Program connected to server side program");
print("------------------------------------------------------")
val=input("\nEnter a number:")
s.send(val.encode())
sdata=s.recv(1024).decode()
print("------------------------------------------------------")
print("Square of {} at Client Side:{}".format(val,sdata))
print("------------------------------------------------------")
