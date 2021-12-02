from Utility.ByteStream import Reader


class CreateAccountMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.DeviceId = self.readString()
        self.FacebookId = self.readString()
        self.GameCenterId = self.readString()
        self.TwitterId = self.readString()
        self.Email = self.readString()


    def process(self):
        pass