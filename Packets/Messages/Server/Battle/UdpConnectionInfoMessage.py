from Utility.ByteStream import Writer


class UdpConnectionInfoMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24112
        self.client = client
        self.player = player


    def encode(self):
        self.writeVInt(9339) # Server Port
        self.writeString("10.0.0.169") # Server Host
        self.writeBytes(b'')
        self.writeBytes(b'')