import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",80))
s.listen(128)
while True:
    a,f=s.accept()
    dat=a.recv(4096)
    a.send(b"HTTP /1.1 200 OK\r\nServer:python\r\n\r\n<h1>test</h1>")
    a.close()
