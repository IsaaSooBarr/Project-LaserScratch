from Packets.Messages.Server.Battle.MatchMakingStatusMessage import MatchMakingStatusMessage
from Packets.Messages.Server.Battle.UdpConnectionInfoMessage import UdpConnectionInfoMessage
from Logic.LogicBattle import LogicBattle
from Utility.ByteStream import Reader
import time


class MatchmakeRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.readDataReference()[1] # Selected Brawler
        self.readVInt() # Event Index
        self.readVInt() # Event Index
        self.readVInt() # Highstakes Index
        self.readVInt()
        

    def process(self):
        MatchMakingStatusMessage(self.client, self.player).send()
        time.sleep(1)
        battle = LogicBattle(self.client, self.player)
        battle.start()