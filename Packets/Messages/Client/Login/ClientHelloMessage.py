from Packets.Messages.Server.Login.ServerHelloMessage import ServerHelloMessage
from Utility.ByteStream import Reader


class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.Protocol = self.readInt()
        self.KeyVersion = self.readInt()
        self.player.Major = self.readInt()
        self.player.Revision = self.readInt()
        self.player.Minor = self.readInt()
        self.ContentHash = self.readString()
        self.DeviceType = self.readInt()
        self.AppStore = self.readInt()
        print("Protocol:", self.Protocol)
        print("Key Version:", self.KeyVersion)
        print("Client Major:", self.player.Major)
        print("Client Minor:", self.player.Revision)
        print("Client Build:", self.player.Minor)
        print("Content Hash:", self.ContentHash)
        print("Device Type:", self.DeviceType)
        print("App Store Type:", self.AppStore)


    def process(self):
        ServerHelloMessage(self.client, self.player).send()