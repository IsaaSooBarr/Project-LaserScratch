from Utility.ByteStream import Writer


class StartLoadingMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559
        self.client = client
        self.player = player


    def encode(self):
        self.writeInt(1) # Game Mode Total Players
        self.writeInt(0)
        self.writeInt(0)
        
        
        # Logic Player Array
        self.writeInt(1) # Players Count
        
        
        self.writeLong(0, 1) # Player ID
        self.writeVInt(1) # Player Index
        self.writeVInt(0) # Player Team
        self.writeVInt(0) 
        self.writeInt(1000000) # ???
        self.writeDataReference(16, 0) # Player Brawler
        self.writeDataReference(29, 0) # Player Skin
        # Logic Hero Upgrades Array
        self.writeBoolean(True) # Hero Upgrades
        self.writeVInt(0) # Brawler Power Level
        self.writeDataReference(23, -1) # Brawler Star Power
        # Logic Hero Upgrades Array End
        # Player Display Data
        self.writeString("Icaro") # Player Name
        self.writeVInt(100)
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        # Player Display Data End
        # Logic Player Array End
        
        
        # Logic Vector Array
        self.writeInt(0) # Array
        for x in range(0):
            self.writeInt(0)
            self.writeInt(0)
        # Logic Vector Array End


        self.writeInt(0) # Count
        
        
        self.writeInt(1413965001) # Unknown
        self.writeVInt(1)
        self.writeVInt(1) # Map Blocks
        self.writeVInt(1) # Joystick Mode
        self.writeBoolean(True) # Battle Hints
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeDataReference(15, 0) # Location ID
        