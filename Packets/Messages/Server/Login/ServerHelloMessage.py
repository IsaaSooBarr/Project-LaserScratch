from Utility.ByteStream import Writer


class ServerHelloMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100
        self.client = client
        self.player = player
        

    def encode(self):
        self.writeInt(24)
        self.writeBytes(b'')
