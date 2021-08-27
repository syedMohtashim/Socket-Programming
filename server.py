# import socket
# from threading import *

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(10)

# connect = True
# while True:
#     # now our endpoint knows about the OTHER endpoint.
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established.")
#     clientsocket.send(bytes("s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)","utf-8"))
#     if connect == False:
#     	

# ip = socket.gethostbyname(socket.gethostname())
# port = 1234
# addr = (ip, port)
# size = 1024
# dis_con_msg = "/Client/Disconnect"
# FORMAT = 'utf-8'

# def new_client(conn, addr):
# 	print(f'[NEW_CONNECTION] {addr} , Status = Connected! ')

# 	con = True
# 	while con:
# 		data = con.recv(size).format(FORMAT)
# 		if data == dis_con_msg:
# 			con = False

# 		print(f"[ {addr} ]  , Data: {data} ")
# 		msg = f"Msg received: {data}"
# 		conn.send(msg.encode(FORMAT))
# 		conn.close()



# def Start():
# 	print("[STARTING] Loading Resources........")
# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 	s.bind(addr)
# 	s.listen()
# 	print(f"[LISTENING] server is listening {ip} : {port}")

# 	while True:
# 	    clientsocket, address = s.accept()
# 	    t1 = Thread(target = new_client, args=(clientsocket,addr))
# 	    t1.start()
# 	    t1.join()
# 	    print(f"[ACTIVE CONNECTIONS] {activeCount() - 1}")


# Start()
import socket
import threading
# import wikipedia

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        msg = f"Msg received: {msg}"
        # msg = wikipedia.summary(msg, sentences=1)
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STATUS] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[STATUS] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()