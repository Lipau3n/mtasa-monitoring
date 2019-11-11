from unittest import TestCase

from mta.monitoring import Server


class TestServerObject(Server):
    def connect(self):
        self.response = b'EYE1\x04mta\x0622003][BS][RU] MTA DayZ Ultimate [#1] "Brown" [HARDCORE, LOOT X1, 130 VEHICLES, FAST ZOMBIE] -TOP-\x14DayZ Ultimate 1.4.7\x05None\x041.5\x020\x024\x0340\x01?\x10[USSR]BadBoy228\x01\x01\x01\x0370\x01?\x07Lesnik\x01\x01\x01\x0332\x01?\tVendetta\x01\x01\x01\x0379\x01?\x05Netx\x01\x01\x01\x0395\x01'


class TestServer(TestCase):
    def setUp(self):
        self.server = TestServerObject('127.0.0.1', 22003)
        super().setUp()

    def test_ase_port(self):
        self.assertEqual(self.server.ase_port, 22126)

    def test_join_link(self):
        self.assertEqual(self.server.join_link, 'mtasa://127.0.0.1:22003')

    def test_socket_addr(self):
        addr = (self.server.address, self.server.ase_port)
        self.assertEqual(self.server.socket_addr, addr)

    def test_read_socket_data(self):
        params = ('game', 'port', 'name', 'gamemode', 'map', 'version', 'somewhat', 'players', 'maxplayers')
        self.assertEqual(self.server.game, 'mta')
        self.assertEqual(self.server.port, '22003')
        self.assertEqual(self.server.name, '[BS][RU] MTA DayZ Ultimate [#1] "Brown" '
                                           '[HARDCORE, LOOT X1, 130 VEHICLES, FAST ZOMBIE] -TOP-')
        self.assertEqual(self.server.gamemode, 'DayZ Ultimate 1.4.7')
        self.assertEqual(self.server.map, 'None')
        self.assertEqual(self.server.version, '1.5')
        self.assertEqual(self.server.somewhat, '0')
        self.assertEqual(self.server.players, '4')
        self.assertEqual(self.server.maxplayers, '40')
