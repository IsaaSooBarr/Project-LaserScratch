from Packets.Messages.Server.Battle.MatchMakingStatusMessage import MatchMakingStatusMessage
from Utility.ByteStream import Reader


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