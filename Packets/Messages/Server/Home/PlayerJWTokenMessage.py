from Utility.ByteStream import Writer


class PlayerJWTokenMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 23774
        self.client = client
        self.player = player


    def encode(self):
        self.writeString("") # JSON Web Token
