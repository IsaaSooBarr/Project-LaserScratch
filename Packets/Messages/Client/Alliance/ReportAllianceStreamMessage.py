from Utility.ByteStream import Reader


class ReportAllianceStreamMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.Id = self.readLong()
        self.ReportedAvatarId = self.readLong()


    def process(self):
        pass