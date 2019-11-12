# MTA Server Monitoring
Multi Theft Auto San Andreas Server Monitoring


## Usage
```python
from mta.monitoring import Server

# pass server address and port
s = Server('46.243.253.51', 22003)

# get current server online and max players
print('{}/{}'.format(s.players, s.maxplayers))
```

## Server information
* **game** (mta)
* **port** - server main port (UDP)
* **ase_port** - server All Seeing Eye port (main MTA:SA port + 123)
* **name** - server name
* **gamemode** - server mode
* **map** - server map
* **version** - mta:sa server version
* **players** - number of players on the server right now
* **maxplayers** - the maximum number of players that can join
