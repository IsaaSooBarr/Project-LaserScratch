from Utility.ByteStream import Writer


class VisionUpdateMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24109
        self.client = client
        self.player = player


    def encode(self):
        self.writeVInt(self.player.BattleTick) # Battle Tick
        self.writeVInt(int(self.player.BattleTick / 10))
        self.writeVInt(0)
        self.writeVInt(0) # Spectates 
        self.writeBoolean(False) # Brawl TV Battle