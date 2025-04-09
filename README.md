# Minecraft Server Status Checker

This Python script checks the status of Minecraft servers (Java and Bedrock versions). It retrieves information such as the server's address, port, version, latency, player statistics, and online/offline status.

## Requirements

- Python 3.6+
- [mcstatus](https://github.com/Dinnerbone/mcstatus) library

You can install the required library using pip:

```bash
pip install mcstatus
```

# Configuration
The script requires a configuration file named servers.cfg. This file should contain the server addresses and ports you want to check.
Example servers.cfg:

```text
[Server1]
server_address = example1.com
server_port = 25565

[Server2]
server_address = example2.com
server_port = 19132
```

# Usage
Run the script using the following command:

```bash
python script_name.py
```

# Output
The script will output server information in JSON format. Example output:
```json
[
    {
        "address": "example1.com",
        "port": "25565",
        "version_name": "1.16.5",
        "version_protocol": 754,
        "latency": 42,
        "player_max": 100,
        "player_online": 10,
        "status": "online",
        "version": "java_version"
    },
    {
        "address": "example2.com",
        "port": "19132",
        "version_name": "1.18.2",
        "version_protocol": 390,
        "latency": 38,
        "player_max": 50,
        "player_online": 5,
        "status": "online",
        "version": "bedrock_version"
    }
]
```

# How It Works
The script:
- Checks if the configuration file servers.cfg exists.
- Reads server information (address and port) from the configuration file.
- Determines if the server is running on the Java or Bedrock edition.
- Queries the server for its status using the mcstatus library.
- Outputs the server's status as JSON.

If a server is offline or inaccessible, the script provides default values indicating its offline status.
