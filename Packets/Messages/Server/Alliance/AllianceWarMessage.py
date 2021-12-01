from Utility.ByteStream import Writer


class AllianceWarMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24776
        self.client = client
        self.player = player


    def encode(self):
        self.writeLong(0, 1) # Player ID
        self.writeVInt(1) # Your Club Faction
        

        # Club War Events Array
        self.writeVInt(1) # Count
        for x in range(1):
            self.writeVInt(0)
            self.writeVInt(0) # Event Column Index
            self.writeVInt(0) # Event Row Index
            self.writeVInt(1) # Club Faction
            self.writeDataReference(15, 0) # War Location ID
            self.writeVInt(1) # War Node State
            self.writeVInt(0) # War Node State Time Left
            self.writeVInt(9) # Faction Score
            self.writeArrayVInt([]) 
        # Club War Events Array End
        

        # Club War Factions Array
        self.writeVInt(1) # Count
        for x in range(1):
            self.writeVInt(1) # Club Faction
            self.writeVInt(1) # Faction Score
        # Club War Factions Array End