from Utility.ByteStream import Reader


class SetDeviceTokenMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.DeviceToken = self.readBytes()
        self.AntihackFlags = self.readInt()


    def process(self):
        pass