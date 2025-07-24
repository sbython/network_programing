import socket

HOST = '127.0.0.1'
PORT = 2548

def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); # craete socket 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # st socket
    s.bind((HOST, PORT)) # link the socket with 127.0.0.1
    s.listen(1) # listen for new connection 
    print("wait for conection")
    return s

s = create_server()

print(HOST+ ":" + str(PORT))

con, adder = s.accept() # accept new connection
while True:
    data = con.recv(1024).decode() # recv the message 
    if data == "quit":
        break
    print(data);
    mess = input(">>")
    con.sendall(mess.encode()) # send the message 
    
s.close() # close socket 