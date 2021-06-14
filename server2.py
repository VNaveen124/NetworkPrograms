#server2.py---------> Server program accept the number from client program and square it send the result to client program
import socket
s=socket.socket()
s.bind( ("localhost",9999) )
s.listen(4)
print("---------------------------------------------------------------")
print("Server Side Program is ready to accept client Request...");
print("---------------------------------------------------------------")
while(True):
	conn,addr=s.accept()
	cval=conn.recv(1024).decode()
	print("Value from client at server side: {}".format(cval))
	n=int(cval)
	res=n*n
	conn.send(str(res).encode())
