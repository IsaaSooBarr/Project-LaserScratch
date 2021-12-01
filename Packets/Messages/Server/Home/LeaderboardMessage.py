from Utility.ByteStream import Writer


class LeaderboardMessage(Writer):
    def __init__(self, client, player, isLocal, Type, BralwerID):
        super().__init__(client)
        self.id = 24403
        self.client = client
        self.player = player
        self.isLocal = isLocal
        self.Type = Type
        self.BralwerID = BralwerID


    def encode(self):
        self.writeVInt(self.Type)
        self.writeDataReference(16, self.BralwerID)
        self.writeString("BR") if self.isLocal == True else self.writeString()


        # Leaderboard Entry Array
        self.writeVInt(1) # Leaderboard Entry Count
        for x in range(1):
            self.writeLogicLong(0, 1) # Target ID
            self.writeVInt(0)
            self.writeVInt(0) # Target Trophies
            # Leaderboard Player Entry
            self.writeBoolean(True) # Leaderboard Player Entry
            self.writeString("Club") # Club Name
            # Player Display Data
            self.writeString("Brawler") # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000) # Player Profile Icon
            self.writeVInt(43000000) # Player Name Color
            # Player Display Data End
            # Leaderboard Player Entry End
            # Leaderboard Alliance Entry
            self.writeBoolean(True) # Leaderboard Alliance Entry
            self.writeString("Club")  # Club Name
            self.writeVInt(1) # Club Members Count
            self.writeDataReference(8, 0) # Club Badge
            # Leaderboard Alliance Entry End
        # Leaderboard Entry Array End
            
            
        self.writeVInt(0)
        self.writeVInt(1) # Leaderboard Entry Count
        self.writeVInt(0)
        self.writeVInt(0) # Leaderboard Global Region
        self.writeString("BR") # Leaderboard Local Region