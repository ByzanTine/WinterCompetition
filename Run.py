#!/usr/bin/python

# This should work in both recent Python 2 and Python 3.

import socket
import json
import struct
import time
import sys
from Player import PlayerT
def sample_bot(host, port):
    s = SocketLayer(host, port)

    gameId = None
    player = None
    while True:
        msg = s.pump()
        
        if msg["type"] == "error":
            print("The server doesn't know your IP. It saw: " + msg["seen_host"])
            sys.exit(1)
        elif msg["type"] == "request":
            if msg["state"]["game_id"] != gameId:
                gameId = msg["state"]["game_id"]
                player = PlayerT()
                print("New game started: " + str(gameId))

            if msg["request"] == "request_card":
                player.requests(msg)
                # cardToPlay = msg["state"]["hand"][0]
                s.send(player.return_response())
            elif msg["request"] == "challenge_offered":
                player.challenge(msg)
                s.send(player.return_response())
                
        elif msg["type"] == "result":
            player.result(msg)

        elif msg["type"] == "greetings_program":
            print("Connected to the server.")

def loop(player, *args):
    while True:
        try:
            player(*args)
        except KeyboardInterrupt:
            sys.exit(0)
        # except Exception as e:
        #     print(repr(e))
        time.sleep(10)

class SocketLayer:
    def __init__(self, host, port):
        self.s = socket.socket()
        self.s.connect((host, port))

    def pump(self):
        """Gets the next message from the socket."""
        sizebytes = self.s.recv(4)
        (size,) = struct.unpack("!L", sizebytes)

        msg = []
        bytesToGet = size
        while bytesToGet > 0:
            b = self.s.recv(bytesToGet)
            bytesToGet -= len(b)
            msg.append(b)

        msg = "".join([chunk.decode('utf-8') for chunk in msg])
        print("Comming Pack: \n %s \n" % msg )
        return json.loads(msg)

    def send(self, obj):
        """Send a JSON message down the socket."""
        b = json.dumps(obj)
        length = struct.pack("!L", len(b))
        self.s.send(length + b.encode('utf-8'))

    def raw_send(self, data):
        self.s.send(data)

if __name__ == "__main__":
    loop(sample_bot, "cuda.contest", 9999)
