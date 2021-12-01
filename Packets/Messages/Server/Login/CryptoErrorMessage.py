from Utility.ByteStream import Writer


class CryptoErrorMessage(Writer):
    def __init__(self, client, player, CryptoError):
        super().__init__(client)
        self.id = 29997
        self.client = client
        self.player = player
        self.CryptoError = CryptoError


    def encode(self):
        self.writeVInt(self.CryptoError) # Crypto Error