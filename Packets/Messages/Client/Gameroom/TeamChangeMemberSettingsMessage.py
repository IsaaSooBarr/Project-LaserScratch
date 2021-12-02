from Utility.ByteStream import Reader


class TeamChangeMemberSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.readVInt()
        self.BrawlerID = self.readDataReference()[1]


    def process(self):
        pass