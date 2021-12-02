from Utility.ByteStream import Reader


class KunlunBillingRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.TID = self.readStringReference()
        self.ProdId = self.readStringReference()
        self.PurchaseToken = self.readStringReference()
        self.Price = self.readStringReference()
        
        
    def process(self):
        pass