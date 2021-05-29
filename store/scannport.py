import socket


def scan_port(ip, port):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	if client.connect_ex((ip, port)):
		pass
	else:
		print(f"Порт {port} открыт")


ip = socket.gethostbyname("ya.ru")
for i in range(81):
	scan_port(ip, i)