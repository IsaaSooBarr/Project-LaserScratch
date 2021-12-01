from Utility.ByteStream import Writer


class AdStatus(Writer):
    def encode(self):
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0) # Used Daily Ads
            self.writeVInt(5) # Maximum Daily Ads