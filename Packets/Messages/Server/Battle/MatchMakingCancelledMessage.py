from Utility.ByteStream import Writer


class MatchMakingCancelledMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20406
        self.client = client
        self.player = player


    def encode(self):
        pass



