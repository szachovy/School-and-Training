import socket
import server
from json import loads

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((server.getConfig('SERVER', 'IPv4'), int(server.getConfig('SERVER', 'port'))))

    while True:
        msg, addr = s.recvfrom(int(server.getConfig('SERVER', 'bytes')))
        fractal = loads(msg.decode('utf-8'))
        for v in fractal.values():
            print(v)

client()