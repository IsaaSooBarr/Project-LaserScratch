from Packets.Messages.Server.Battle.VisionUpdateMessage import VisionUpdateMessage
from Packets.Messages.Server.Battle.StartLoadingMessage import StartLoadingMessage
from Packets.Messages.Server.Battle.UdpConnectionInfoMessage import UdpConnectionInfoMessage
import time
from threading import Thread


class LogicBattle(Thread):
    def __init__(self, client, player):
        Thread.__init__(self)
        self.client = client
        self.player = player
        self.subTick = 0
        self.tick = 0
        self.started = 0
    

    def run(self):
        self.startBattle()
    

    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.client, self.player).send()
        UdpConnectionInfoMessage(self.client, self.player).send()
        while self.started:
            if self.subTick >= 4:
                self.tick += 1
                self.subTick = 0
                self.player.BattleTick = self.tick
            self.process()
            time.sleep(0.003)


    def process(self):
        VisionUpdateMessage(self.client, self.player).send()
        self.subTick += 1