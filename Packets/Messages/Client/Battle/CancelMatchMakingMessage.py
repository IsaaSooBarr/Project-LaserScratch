from Packets.Messages.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage
from Utility.ByteStream import Reader


class CancelMatchMakingMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        pass
        

    def process(self):
        MatchMakingCancelledMessage(self.client, self.player).send()