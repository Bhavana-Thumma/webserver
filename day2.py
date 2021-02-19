import socket
import os
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
	request = conn.recv(1024)
	print(request.decode('utf-8'))
	lines = request.decode('utf-8').split('\n')
	print(lines)
	filename = lines[0].split()[1]
	if( filename == '/'):
		filename ='/index.html'
	try:
		l=["html", "txt"]
		if(filename == "/log"):
			content ="<CENTER><h1>Forbidden Page<h1><CENTER>"
			response ="HTTP/1.1 403 FORBIDDEN\nContent-Type: text/html\n\n"+content
		elif(filename.split(".")[1] not in l):
			content ="<CENTER><h1>Unsupported Media Type<h1><CENTER>"
			response ="HTTP/1.1 415 MEDIATYPE\nContent-Type: text/html\n\n"+content
		else:
			fin = open(filename[1:])
			content = fin.read()
			fin.close()
			response ="HTTP/1.1 200 OK\nContent-Type: text/html\n\n"+content
	except FileNotFoundError:
		content ="<CENTER><h1>File Not Found<h1><CENTER>"
		response = 'HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n'+content

	conn.sendall(response.encode())
	conn.close()
print("Done!!!")
soc.close()

