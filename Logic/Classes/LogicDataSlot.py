from Utility.ByteStream import Writer


class LogicDataSlotHeroOrItemUnlocked(Writer):
    def encode(self):
        self.writeVInt(1 + 7) # Items Count
        for x in range(1):
            self.writeDataReference(23, x) # Item ID
            self.writeVInt(1) # Item Data
        self.writeDataReference(5, 1) # Resource ID
        self.writeVInt(0) # Tokens Amount
        self.writeDataReference(5, 5) # Resource ID
        self.writeVInt(0) # Chips Amount
        self.writeDataReference(5, 6) # Resource ID
        self.writeVInt(0) # Elixir Amount
        self.writeDataReference(5, 7) # Resource ID
        self.writeVInt(0) # Upgrade Tokens Amount
        self.writeDataReference(5, 8) # Resource ID
        self.writeVInt(0) # Coins Amount
        self.writeDataReference(5, 9) # Resource ID
        self.writeVInt(0) # Star Tokens Amount
        self.writeDataReference(5, 10) # Resource ID
        self.writeVInt(0) # Star Points Amount


class LogicDataSlotHeroScore(Writer):
    def encode(self):
        self.writeVInt(0) # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0) # Brawler ID
            self.writeVInt(0) # Brawler Trophies


class LogicDataSlotHeroHighestScore(Writer):
    def encode(self):
        self.writeVInt(0) # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0) # Brawler ID
            self.writeVInt(0) # Brawler Highest Trophies


class LogicDataSlotResourceCount(Writer):
    def encode(self):
        self.writeVInt(0) # Resources Count
        for x in range(0):
            self.writeDataReference(5, 0) # Resource ID
            self.writeVInt(0) # Resource Amount


class LogicDataSlotHeroPower(Writer):
    def encode(self):
        self.writeVInt(0) # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0) # Brawler ID
            self.writeVInt(0) # Brawler Power Points Amount


class LogicDataSlotHeroLevel(Writer):
    def encode(self):
        self.writeVInt(0) # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0) # Brawler ID
            self.writeVInt(0) # Brawler Power Level


class LogicDataSlotCardCount(Writer):
    def encode(self):
        self.writeVInt(0) # Items Count
        for x in range(0):
            self.writeDataReference(23, 0) # Item ID
            self.writeVInt(0) # Item Data


class LogicDataSlotHeroSeenState(Writer):
    def encode(self):
        self.writeVInt(0) # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0) # Brawler ID
            self.writeVInt(0) # Brawler Seem State