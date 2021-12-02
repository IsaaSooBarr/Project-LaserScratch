from Utility.ByteStream import Reader


class TeamSetMemberReadyMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.readBoolean()
        self.readVInt()


    def process(self):
        pass