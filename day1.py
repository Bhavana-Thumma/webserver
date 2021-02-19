import socket,requests
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = ''
port = 1234
print("<<<<<<< Server started >>>>>")
soc.bind((ip, port))
print(f"Port:{port}")
soc.listen(1)
while(True):
	conn, addr = soc.accept()
	data = conn.recv(1024)
	print(data.decode('utf-8'))
	response ="""
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello world!</h1>
<b>This is my first webserver program</b>
"""
	conn.sendall(response.encode())
	conn.close()
print("Done!!!")
soc.close()

