from Utility.ByteStream import Reader


class AnalyticEventMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.Type = self.readStringReference()
        self.Event = self.readString()


    def process(self):
        print("[INFO] " + self.Type + " " + self.Event)