from mcstatus import BedrockServer, JavaServer
from mcstatus.status_response import BedrockStatusResponse, JavaStatusResponse
import asyncio
import json
import os
import configparser


config_file = "servers.cfg"

if os.path.exists(config_file):
   cfg = configparser.RawConfigParser()
   cfg.read(config_file)
else:
    print(f"No configuration file found, {config_file} do not exist.")
    exit()


def test_server (srv_add, srv_port):
    server_status = {}

    try:
        try:
            server = JavaServer(srv_add, int(srv_port))
            status = server.status()

            server_status["address"] = srv_add
            server_status["port"] = srv_port
            server_status["version_name"] = status.version.name
            server_status["version_protocol"] = status.version.protocol
            server_status["latency"] = int(status.latency)
            server_status["player_max"] = status.players.max
            server_status["player_online"] = status.players.online
            server_status["status"] = 'online'
            server_status["version"] = 'java_version'

        except:
            server = BedrockServer(srv_add, int(srv_port))
            status = server.status()

            server_status["address"] = srv_add
            server_status["port"] = srv_port
            server_status["version_name"] = status.version.name
            server_status["version_protocol"] = status.version.protocol
            server_status["latency"] = int(status.latency)
            server_status["player_max"] = status.players.max
            server_status["player_online"] = status.players.online
            server_status["status"] = 'online'
            server_status["version"] = 'bedrock_version'

    except:
        server_status["address"] = srv_add
        server_status["port"] = srv_port
        server_status["version_name"] = 'Null'
        server_status["version_protocol"] = 'Null'
        server_status["latency"] = 0
        server_status["player_max"] = 'Null'
        server_status["player_online"] = 'Null'
        server_status["status"] = 'offline'
        server_status["version"] = 'Null'

    return server_status


if __name__ == '__main__':
    all_server_info = []

    for section in cfg.sections():
        server_info = test_server(cfg.get(section, 'server_address'), cfg.get(section, 'server_port'))
        all_server_info.append(server_info)


    print(json.dumps(all_server_info, indent=4))