from Packets.Messages.Server.Home.LeaderboardMessage import LeaderboardMessage
from Utility.ByteStream import Reader


class GetLeaderboardMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.isLocal = self.readBoolean()
        self.Type = self.readVInt()
        self.BralwerID = self.readDataReference()[1]


    def process(self):
        LeaderboardMessage(self.client, self.player, self.isLocal, self.Type, self.BralwerID).send()