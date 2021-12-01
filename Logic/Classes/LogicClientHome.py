from Logic.Classes.LogicDailyData import LogicDailyData
from Logic.Classes.LogicConfData import LogicConfData
from Utility.ByteStream import Writer


class LogicClientHome(Writer):
    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)
        self.writeLong(0, 1) # Home ID


        self.writeVInt(16) # Notification Factory
        

        # New Brawler Ranks Notification
        self.writeVInt(78) # Notification ID
        self.writeInt(0) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(400) # Star Points Gained
        self.writeVInt(50) # Tokens Gained
        # New Brawler Ranks Notification End
        

        # Season End Notification
        self.writeVInt(79) # Notification ID
        self.writeInt(1) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(28) # Brawlers Count
        for x in range(28):
            self.writeVInt(16000000 + x) # Brawler ID
            self.writeVInt(1400) # Brawler Trophies
            self.writeVInt(450) # Brawler Trophy Loss
            self.writeVInt(480) # Star Points Gained
        # Season End Notification End

        
        # Star Points Migration Notification 
        self.writeVInt(80) # Notification ID
        self.writeInt(2) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(8000) # Star Points Gained
        # Star Points Migration Notification End
        
        
        # Custom Support Message Notification
        self.writeVInt(81) # Notification ID
        self.writeInt(3) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString("Hacc") # Notification Message Entry
        self.writeVInt(0)
        # Custom Support Message Notification End
        
        
        # Club Mail Notification
        self.writeVInt(82) # Notification ID
        self.writeInt(4) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString("Hacc") # Message Entry
        # Player Display Data
        self.writeString("Brawler") # Player Name
        self.writeVInt(100)
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        # Player Display Data End
        # Club Mail Notification End

        
        # Promo Popup Notification
        self.writeVInt(83) # Notification ID
        self.writeInt(5) # Notification Index
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.ChronosTextEntry(0, "Welcome to LaserScratch!") # Primary Text Entry
        self.ChronosTextEntry(0, "Check GitHub for more info and updates!") # Secondary Text Entry
        self.ChronosTextEntry(0, "View More") # Button Text Entry
        self.ChronosFileEntry("pop_up_1920x1235_welcome.png", "6bb3b752a80107a14671c7bdebe0a1b662448d0c") # Notification Banner Data
        self.writeStringReference("brawlstars://extlink?page=https%3A%2F%2Fgithub.com%2FIcaro072%2FProject-LaserScratch") # Notification Event
        self.writeVInt(0)
        # Promo Popup Notification End

        
        # Star Power Donated Notification
        self.writeVInt(84) # Notification ID
        self.writeInt(6) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0) 
        self.writeVInt(23000000 + 76) # Star Power Donated
        # Star Power Donated Notification End
        
        
        # Gems Refunded Notification
        self.writeVInt(85) # Notification ID
        self.writeInt(7) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0) # Revoke Type
        self.writeVInt(0) # Gems Revoked
        self.writeLong(0, 1) # Player ID
        self.writeVInt(0) 
        self.writeString("") # Offer Purchased Timestamp
        # Gems Refunded Notification End
        

        # News Notification
        self.writeVInt(87) # Notification ID
        self.writeInt(8) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeStringReference()
        # News Notification End

        
        # Token Doubler Donated Notification
        self.writeVInt(88) # Notification ID
        self.writeInt(9) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0)
        self.writeVInt(0) # Token Doublers Donated
        # Token Doubler Donated Notification End
        

        # Gems Donated Notification
        self.writeVInt(89) # Notification ID
        self.writeInt(10) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0)
        self.writeVInt(0) # Gems Donated
        # Gems Donated Notification End
        

        # Resource Donated Notification
        self.writeVInt(90) # Notification ID
        self.writeInt(11) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0)
        self.writeVInt(5000000 + 1) # Resource ID
        self.writeVInt(0) # Resource Donated
        # Resource Donated Notification End
        

        # Tickets Donated Notification
        self.writeVInt(91) # Notification ID
        self.writeInt(12) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0)
        self.writeVInt(0) # Token Doublers Donated
        # Tickets Donated Notification End
        

        # Brawler Power Points Donated Notification
        self.writeVInt(92) # Notification ID
        self.writeInt(13) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0)
        self.writeVInt(16000000 + 0) # Brawler ID
        self.writeVInt(0) # Power Points Donated
        # Brawler Power Points Donated Notification End
        

        # Brawler Donated Notification
        self.writeVInt(93) # Notification ID
        self.writeInt(14) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(0) 
        self.writeVInt(16000000 + 0) # Brawler Donated
        # Brawler Donated Notification End
        

        # Skin Donated Notification
        self.writeVInt(94) # Notification ID
        self.writeInt(15) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVInt(29000000 + 2) # Skin Donated
        # Skin Donated Notification End
        
        
        self.writeVInt(-1)
        self.writeBoolean(False)
        
        
        # Gatcha Drop Array 
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(16, -1)
            self.writeVInt(0)
            self.writeDataReference(29, -1)
            self.writeDataReference(23, -1)
            self.writeVInt(0)
        # Gatcha Drop Array End