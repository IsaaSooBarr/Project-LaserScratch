from Utility.ByteStream import Reader


class ResetAccountMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.AccountPreset = self.readInt()


    def process(self):
        pass