from Utility.ByteStream import Reader


class ReportUserMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.readInt()
        self.ReportedAvatarId = self.readLong()


    def process(self):
        pass