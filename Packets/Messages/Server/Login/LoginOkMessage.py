from Utility.ByteStream import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20104
        self.client = client
        self.player = player


    def encode(self):
        self.writeLong(0, 1) # Account ID
        self.writeLong(0, 1) # Home ID
        self.writeString("") # Pass Token
        self.writeString() # Facebook ID
        self.writeString() # Gamecenter ID
        self.writeInt(self.player.Major) # Server Major Version
        self.writeInt(self.player.Revision) # Server Build Version
        self.writeInt(self.player.Minor) # Content Version 
        self.writeString("dev") # Environment
        self.writeInt(0) # Session Count
        self.writeInt(0) # Play Time Seconds
        self.writeInt(0) # Days Since Started Playing
        self.writeString("103121310241222") # Facebook Application ID
        self.writeString("") # Server Time
        self.writeString("") # Account Created Date
        self.writeInt(0) # Startup Cooldown
        self.writeString() # Google Service ID
        self.writeString("BR") # Login Country
        self.writeString() # Kunlun ID 
        self.writeInt(2) # Tier
        self.writeString("")
        self.writeInt(2) # Url Entry Array Count
        self.writeString("https://game-assets.brawlstarsgame.com")
        self.writeString("http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com")
        self.writeInt(2) # Url Entry Array Count
        self.writeString("https://raw.githubusercontent.com/IsaaSooBart/Project-LaserScratch/main/Files/EventAssets/") # Event Assets
        self.writeString("https://24b999e6da07674e22b0-8209975788a0f2469e68e84405ae4fcf.ssl.cf2.rackcdn.com/event-assets")
        self.writeVInt(0) # Seconds Until Account Deletion
        self.writeCompressedString(b'') # Supercell ID Token
        self.writeBoolean(True,False) # Double Boolean
        self.writeString("")
