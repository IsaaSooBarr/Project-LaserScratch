from Packets.Messages.Server.Login.CryptoErrorMessage import CryptoErrorMessage
from Utility.ByteStream import Reader


class ClientCryptoErrorMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.CryptoError = self.readInt()


    def process(self):
        CryptoErrorMessage(self.client, self.player, self.CryptoError).send()
