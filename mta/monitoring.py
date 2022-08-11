import socket
from typing import Optional, Tuple

from mta.exceptions import ServerException


class Server:
    timeout: float = .2
    game: Optional[str] = None
    port: Optional[int] = None
    name: Optional[str] = None
    gamemode: Optional[str] = None
    map: Optional[str] = None
    version: Optional[str] = None
    somewhat: Optional[str] = None
    players: Optional[str] = None
    maxplayers: Optional[str] = None

    def __init__(self, address: str, port: int = 22003, **kwargs):
        self.validate_address(address)
        self.address = address
        self.port = port
        self.ase_port = port + 123
        self.__dict__.update(kwargs)
        self.response = None
        self.connect()
        self.read_socket_data()

    @staticmethod
    def validate_address(address: str):
        try:
            socket.inet_aton(address)
        except socket.error as e:
            raise ServerException('Invalid server address. Original exception: %s' % e.strerror)

    @property
    def join_link(self) -> str:
        """
        Return link to join MTA:SA server
        """
        return 'mtasa://{}:{}'.format(self.address, self.port)

    @property
    def socket_addr(self) -> Tuple[str, int]:
        return self.address, self.ase_port

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)
        try:
            sock.connect(self.socket_addr)
            sock.send(b"s")
            self.response = sock.recv(16384)
        except socket.error as e:
            raise ServerException("Cant't connect to server. Original exception: %s" % str(e))
        finally:
            sock.close()

    def read_row(self, start: int) -> (int, str):
        start_end = start + 1
        length = ord(self.response[start:start_end]) - 1
        value = self.response[start_end:start_end + length]
        return start_end + length, value.decode('utf-8')

    def read_socket_data(self):
        start = 4
        params = ('game', 'port', 'name', 'gamemode', 'map', 'version', 'somewhat', 'players', 'maxplayers')
        for param in params:
            start, value = self.read_row(start)
            setattr(self, param, value)
