from Packets.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Utility.ByteStream import Reader


class GetPlayerProfileMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.PlayerID = self.readLong()


    def process(self):
        self.HighID = self.PlayerID[0]
        self.LowID = self.PlayerID[1]
        PlayerProfileMessage(self.client, self.player, self.HighID, self.LowID).send()
