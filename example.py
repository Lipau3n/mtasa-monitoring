from mta.monitoring import Server

# pass server address and port
s = Server('46.243.253.51', 22003)

# get current server online and max players
print('{}/{}'.format(s.players, s.maxplayers))
