from Packets.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Utility.ByteStream import Reader


class GoHomeMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.ClearActiveBattle = self.readBoolean()


    def process(self):
        OwnHomeDataMessage(self.client, self.player).send()