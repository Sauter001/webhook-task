import socket
import time

IP_ADDR = "0.0.0.0"
TCP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP_ADDR, TCP_PORT))
sock.listen()

while True:
    conn, addr = sock.accept()
    print(f"Client address: {addr}")
    data = conn.recv(BUFFER_SIZE)
    # if not data: break
    currentTime = "".join([" ", "test ", time.ctime(time.time()), "\r\n"])
    print(data.decode("utf-8"))
    data += currentTime.encode("ascii")
    conn.send(data)  # echo
    conn.close()
