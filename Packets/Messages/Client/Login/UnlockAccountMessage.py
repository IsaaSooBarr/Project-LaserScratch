from Utility.ByteStream import Reader


class UnlockAccountMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.AccountID = self.readLong()
        self.PassToken = self.readString()
        self.UnlockCode = self.readString()
        self.SupercellIDToken = self.readString()
        
        
    def process(self):
        self.HighID = self.AccountID[0]
        self.LowID = self.AccountID[1]