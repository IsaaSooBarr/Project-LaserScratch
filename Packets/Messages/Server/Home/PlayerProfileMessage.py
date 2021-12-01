from Utility.ByteStream import Writer


class PlayerProfileMessage(Writer):
    def __init__(self, client, player, HighID, LowID):
        super().__init__(client)
        self.id = 24113
        self.client = client
        self.player = player
        self.HighID = HighID
        self.LowID = LowID


    def encode(self):
         # Player Profile
        self.writeLogicLong(self.HighID, self.LowID) # Player ID
        self.writeDataReference(0, -1)
                
                
        # Hero Entry Array
        self.writeVInt(1) # Brawlers Count
        for x in range(1):
            self.writeDataReference(16, x) # Brawler ID
            self.writeDataReference(29, -1) # Skin ID
            self.writeVInt(0) # Brawler Trophies
            self.writeVInt(0) # Brawler Trophies for Rank
            self.writeVInt(1) # Brawler Power Level
        # Hero Entry Array End
                
                
        # Stats Entry Array
        self.writeVInt(11) # Stats Count
        self.writeVInt(1) # Stats Index
        self.writeVInt(0) # 3 vs 3 Victories
        self.writeVInt(2) # Stats Index
        self.writeVInt(0) # Player Experience Points
        self.writeVInt(3) # Stats Index
        self.writeVInt(0) # Player Trophies
        self.writeVInt(4) # Stats Index
        self.writeVInt(0) # Player Highest Trophies
        self.writeVInt(5) # Stats Index
        self.writeVInt(1) # Unlocked Brawlers
        self.writeVInt(6) # Stats Index
        self.writeVInt(0) # Unknown
        self.writeVInt(7) # Stats Index
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(8) # Stats Index
        self.writeVInt(0) # Solo Victories
        self.writeVInt(9) # Stats Index
        self.writeVInt(0) # Best Robo Rumble Time
        self.writeVInt(10) # Stats Index
        self.writeVInt(0) # Best Time As Big Brawler
        self.writeVInt(11) # Stats Index
        self.writeVInt(0) # Duo Victories
        # Stats Entry Array End


        # Player Display Data
        self.writeString("Brawler") # Player Name
        self.writeVInt(100)
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        # Player Display Data End
        # Player Profile End
                

        # Club Header Entry Array
        self.writeBoolean(True) # Joined In a Club
        self.writeLong(0, 1) # Club ID
        self.writeString("Club") # Club Name
        self.writeDataReference(8, 0) # Club Badge
        self.writeVInt(1) # Club Type
        self.writeVInt(1) # Club Members
        self.writeVInt(0) # Club Trophies
        self.writeVInt(0) # Club Required Trophies
        self.writeDataReference(0, 0)
        self.writeString("BR") # Club Region
        self.writeVInt(1) # Club Online Members
        # Club Header Entry Array End


        self.writeDataReference(25, 1) # Club Role