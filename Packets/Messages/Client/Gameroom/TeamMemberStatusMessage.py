from Utility.ByteStream import Reader


class TeamMemberStatusMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.Status = self.readVInt()


    def process(self):
    	pass

