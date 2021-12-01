from Utility.ByteStream import Writer


class IntValueEntryLogicDailyData(Writer):
    def encode(self):
        self.writeVInt(9) # Home Events Count
        self.writeLong(1, False) # Daily Created Club State
        self.writeLong(2, False) # Daily Changed Location State
        self.writeLong(3, 0) # Tokens Gained
        self.writeLong(4, 0) # Trophies Gained
        self.writeLong(5, 0) # Star Tokens Gained
        self.writeLong(6, False) # Demo Account State
        self.writeLong(7, False) # Do Not Disturb State
        self.writeLong(8, 0) # Star Points Gained
        self.writeLong(9, False) # Star Points Enabled State


class IntValueEntryLogicConfData(Writer):
    def encode(self):
        self.writeVInt(6) # Home Events Count
        self.writeLong(1, 41000000) # Menu Theme
        self.writeLong(3, 3) # Level Required For Unlock Friendly Games
        self.writeLong(5, False) # Temporarily Disable Shop
        self.writeLong(6, False) # Temporarily Disable Brawl Boxes
        self.writeLong(14, False) # Double Token Weekend
        self.writeLong(15, True) # Disable Content Creator Boost