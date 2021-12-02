from Utility.ByteStream import Reader


class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.EventSlot = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readBoolean()


    def process(self):
        pass