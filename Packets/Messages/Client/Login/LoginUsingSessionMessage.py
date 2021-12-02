from Utility.ByteStream import Reader


class LoginUsingSessionMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.AccountIdHigherInt = self.readInt()
        self.AccountIdLowerInt = self.readInt()
        self.SessionKey = self.readString()
        self.FacebookAccessToken = self.readString()
        self.Source = self.readString()
        self.DeviceIdentifier = self.readString()
        self.DeviceToken = self.readString()


    def process(self):
        pass