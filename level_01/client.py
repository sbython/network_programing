import socket

HOST = '127.0.0.1'
PORT = 2548

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # set socket 
s.connect((HOST, PORT)) # connect wiht server 127.0.0.1;1548
while True:
     mess = input(">>") 
     s.sendall(mess.encode()) # send message
     if mess == 'quit':
          break
     print(s.recv(1024).decode()) # recv messge and print it 

s.close() #close socket
