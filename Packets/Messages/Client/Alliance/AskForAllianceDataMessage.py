from Packets.Messages.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Utility.ByteStream import Reader


class AskForAllianceDataMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.AllianceID = self.readLong()
        self.readBoolean()


    def process(self):
        self.HighID = self.AllianceID[0]
        self.LowID = self.AllianceID[1]
        AllianceDataMessage(self.client, self.player, self.HighID, self.LowID).send()