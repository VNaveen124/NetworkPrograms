#server1.py
import socket
s=socket.socket()
s.bind( ("localhost",8989) )
s.listen(4)
print("---------------------------------------------------------------")
print("Server Side Program is ready to accept client Request...");
print("---------------------------------------------------------------")
while(True):
	con,addr=s.accept()
	print("Type of con=",type(con))
	print("Type of addr=",type(addr))
	print("Server program connected to client at: {}".format(addr))
	print("--------------------------------------------------------------")
	cdata=con.recv(1024).decode()
	print("Data from Client at Server side={}".format(cdata))
	print("--------------------------------------------------------------")
	con.send("Hi, This is KVR from server Side".encode())
