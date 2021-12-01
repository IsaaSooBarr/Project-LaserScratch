from Utility.ByteStream import Writer


class MyAllianceMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24399
        self.client = client
        self.player = player


    def encode(self):
        self.writeVInt(1)
        self.writeBoolean(True) # Joined In a Club
        self.writeDataReference(25, 1) # Club Role
        # Club Header Entry
        self.writeLong(0, 1) # Club ID
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