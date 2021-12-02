from Utility.ByteStream import Reader


class TencentBillingRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.OriginalJSON = self.readStringReference()
        self.Signature = self.readStringReference()
        self.ProdId = self.readStringReference()
        self.Price = self.readStringReference()
        
        
    def process(self):
        pass