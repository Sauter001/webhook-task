import socket

IP = input("Server address: ")
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = ""

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, TCP_PORT))
    MESSAGE = input("Write to server: ")
    if MESSAGE == "q":
        break
    sock.send(MESSAGE.encode("utf-8"))
    print(f"Sending data: {MESSAGE}")
    data = sock.recv(BUFFER_SIZE)
    print("Data from server:", data.decode("utf-8"))

sock.close()
