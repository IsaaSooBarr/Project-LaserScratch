from Packets.Messages.Server.Home.PlayerJWTokenMessage import PlayerJWTokenMessage
from Utility.ByteStream import Reader


class AskPlayerJWTokenMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass


    def process(self):
        PlayerJWTokenMessage(self.client, self.player).send()