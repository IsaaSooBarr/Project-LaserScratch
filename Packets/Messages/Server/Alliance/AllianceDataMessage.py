from Utility.ByteStream import Writer


class AllianceDataMessage(Writer):
    def __init__(self, client, player, HighID, LowID):
        super().__init__(client)
        self.id = 24301
        self.client = client
        self.player = player
        self.HighID = HighID
        self.LowID = LowID


    def encode(self):
        self.writeBoolean(False) 
        # Club Full Entry
        # Club Header Entry
        self.writeLong(self.HighID, self.LowID) # Club ID
        self.writeString("Club") # Club Name
        self.writeDataReference(8, 0) # Club Badge
        self.writeVInt(1) # Club Type
        self.writeVInt(1) # Club Members
        self.writeVInt(0) # Club Trophies
        self.writeVInt(0) # Club Required Trophies
        self.writeDataReference(0, -1)
        self.writeString("BR") # Club Region
        self.writeVInt(1) # Club Online Members
        # Club Header Entry End
        self.writeString("Club Description") # Club Description


        # Club Members Array
        self.writeVInt(1) # Club Members Count
        for x in range(1):
            self.writeLong(0, 1) # Player ID
            self.writeVInt(1) # Player Club Role
            self.writeVInt(0) # Player Trophies
            self.writeVInt(8) # Player Status
            self.writeVInt(0) # Player Status Timer
            self.writeBoolean(False)
            # Player Display Data
            self.writeString("Brawler") # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000) # Player Profile Icon
            self.writeVInt(43000000) # Player Name Color
            # Player Display Data End
        # Club Members Array End
        # Club Full Entry End