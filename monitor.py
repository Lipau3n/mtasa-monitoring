import socket
from typing import Dict

port = 22003
host = '46.243.253.51'
remote_addr = (host, port + 123)


def read_row(start: int, response: bytes) -> (int, str):
    start_end = start + 1
    length = ord(response[start:start_end]) - 1
    value = response[start_end:start_end + length]
    return start_end + length, value.decode('utf-8')


def read_socket_data(response: bytes) -> Dict:
    start = 4
    data = {}
    start, data['game'] = read_row(start, response)
    start, data['port'] = read_row(start, response)
    start, data['name'] = read_row(start, response)
    start, data['gamemode'] = read_row(start, response)
    start, data['map'] = read_row(start, response)
    start, data['version'] = read_row(start, response)
    start, data['somewhat'] = read_row(start, response)
    start, data['players'] = read_row(start, response)
    start, data['maxplayers'] = read_row(start, response)
    return data


data = None
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(.2)
try:
    sock.connect(remote_addr)
    sock.send(b"s")
    response = sock.recv(16384)
    data = read_socket_data(response)
except Exception as e:
    print(e)
finally:
    sock.close()
