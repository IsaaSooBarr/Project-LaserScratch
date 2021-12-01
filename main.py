import logging
import socket
import time
import os
from threading import *
from Logic.Device import Device
from Logic.Player import Players
from Utility.Utils import Utils
from Packets.LogicLaserFactory import AvailablePackets
from Packets.Messages.Server.Home.LobbyInfoMessage import LobbyInfoMessage


def _(*args):
    print('[INFO]', end=' ')
    for arg in args:
        print(arg, end=' ')
    print()



class Server:
    Clients = {"ClientCounts": 0, "Clients": {}}
    ThreadCount = 0
    
    
    def __init__(self, ip: str, port: int):
        self.server = socket.socket()
        self.port = port
        self.ip = ip


    def start(self):
        self.server.bind((self.ip, self.port))
        _(f'Server started! Ip: {self.ip}, Port: {self.port}')
        while True:
            self.server.listen()
            client, address = self.server.accept()
            _(f'New connection! Ip: {address[0]}')
            ClientThread(client, address).start()
            Utils.connected_clients['ClientsCount'] += 1


class ClientThread(Thread):
    def __init__(self, client, address):
        super().__init__()
        self.client = client
        self.address = address
        self.device = Device(self.client)
        self.player = Players(self.device)


    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            s = self.client.recv(length)
            if not s:
                print("Receive Error!")
                break
            data += s
        return data


    def run(self):
        LastPacketRecived = time.time()
        try:
            while True:
                header = self.client.recv(7)
                if len(header) > 0:
                    LastPacketRecived = time.time()
                    PacketID = int.from_bytes(header[:2], 'big')
                    PacketLenght = int.from_bytes(header[2:5], 'big')
                    PacketData = self.recvall(PacketLenght)
                    LobbyInfoMessage(self.client, self.player, Utils.connected_clients['ClientsCount']).send()
                    if PacketID in AvailablePackets:
                        PacketName = AvailablePackets[PacketID].__name__
                        _(f'Packet {PacketID}: {PacketName} was received!')
                        message = AvailablePackets[PacketID](self.client, self.player, PacketData)
                        message.decode()
                        message.process()
                        if PacketID == 10101:
                            Server.Clients["Clients"][str(self.player.low_id)] = {"SocketInfo": self.client}
                            Server.Clients["ClientCounts"] = Server.ThreadCount
                            self.player.ClientDict = Server.Clients
                    else:
                        _(f'Packet {PacketID} is not handled!')
                if time.time() - LastPacketRecived > 10:
                    print(f"[INFO] Ip: {self.address[0]} disconnected!")
                    self.client.close()
                    break
        except ConnectionAbortedError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()
        except ConnectionResetError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()
        except TimeoutError:
            print(f"[INFO] Ip: {self.address[0]} disconnected!")
            self.client.close()


if __name__ == '__main__':
    server = Server('0.0.0.0', 9339)
    server.start()