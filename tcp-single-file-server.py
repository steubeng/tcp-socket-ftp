import socket

if __name__ == '__main__':
	# Defining Socket
	host = 'localhost'
	port = 8080
	# totalclient = int(input('Enter number of clients: '))
	totalclient = 1

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host, port))
	sock.listen(totalclient)
	# Establishing Connections
	connections = []
	print('Initiating clients')
	for i in range(totalclient):
		conn = sock.accept()
		connections.append(conn)
		print('Connected with client', i+1)
		print('Connected with client')

	fileno = 0
	idx = 0
	for conn in connections:
		# Receiving File Data
		idx += 1
		data = conn[0].recv(1024).decode()

		if not data:
			continue
	# Creating a new file at server end and writing the data
		filename = 'received.file'
		fileno = fileno+1
		fo = open(filename, "w")
		# print('Receiving file from client', idx)
		print('Receiving file from client')
		i=1
		while data:
			if not data:
				break
			else:
				if (i % 100 == 0):
					print('.', end="", flush=True)
				if (i % (80 * 100) == 0):
					print(flush=True)
				i+=1
				fo.write(data)
				data = conn[0].recv(1024).decode()

		print()
		print()
		print('Received successfully! New filename is:', filename)
		fo.close()
	# Closing all Connections
	for conn in connections:
		conn[0].close()
