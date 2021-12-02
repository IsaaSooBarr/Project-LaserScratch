from Utility.ByteStream import Reader


class AppleBillingRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.TID = self.readString()
        self.ProdId = self.readString()
        self.CurrencyCode = self.readString()
        self.Price = self.readString()
        #self.ReceiptDataLength = self.readBytes()
        
        
    def process(self):
        pass