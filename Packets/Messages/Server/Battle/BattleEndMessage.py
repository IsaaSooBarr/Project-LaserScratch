from Utility.ByteStream import Writer


class BattleEndMessage(Writer):
    def __init__(self, client, player, Type):
        super().__init__(client)
        self.id = 23456
        self.client = client
        self.player = player
        self.Type = Type


    def encode(self):
        self.writeVInt(self.Type) # Battle End Game Mode 
        self.writeVInt(self.player.BattleResult) # Battle Result 
        self.writeVInt(0) # Tokens Gained
        self.writeVInt(0) # Trophies Result 
        self.writeVInt(0) # Doubled Tokens
        self.writeVInt(0) # Double Token Weekend
        self.writeVInt(0) # Token Doubler Remaining
        self.writeVInt(0) # Ticketed Events Extra Data
        self.writeBoolean(False,False,False,False,False,False) # Battle End Type


        # Player Entry Array
        self.writeVInt(self.player.BattlePlayers) # Battle Players
        self.writeBoolean(True,False,False) # Team And Star Player Type
        self.writeDataReference(16, self.player.BrawlerID) # Player Brawler
        self.writeDataReference(29, self.player.SkinID) # Player Skin
        self.writeVInt(0) # Brawler Trophies
        self.writeVInt(1) # Brawler Power Level
        self.writeBoolean(True) # IsPlayer Array
        self.writeLong(0, 1) # Player ID
        # Player Display Data
        self.writeString("Icaro") # Player Name
        self.writeVInt(100) 
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        # Player Display Data End
            
            
        BotName = [self.player.Bot1Name, self.player.Bot2Name, self.player.Bot3Name, self.player.Bot4Name, self.player.Bot5Name, self.player.Bot6Name, self.player.Bot7Name, self.player.Bot8Name, self.player.Bot9Name]
        BotTeam = [self.player.Bot1Team, self.player.Bot2Team, self.player.Bot3Team, self.player.Bot4Team, self.player.Bot5Team, self.player.Bot6Team, self.player.Bot7Team, self.player.Bot8Team, self.player.Bot9Team]
        BotBrawler = [self.player.Bot1Brawler, self.player.Bot2Brawler, self.player.Bot3Brawler, self.player.Bot4Brawler, self.player.Bot5Brawler, self.player.Bot6Brawler, self.player.Bot7Brawler, self.player.Bot8Brawler, self.player.Bot9Brawler]
        for PlayerIndex in range(self.player.BattlePlayers - 1):
            if self.player.PlayerTeam == 0:
                if BotTeam[PlayerIndex] == 0:
                    self.writeBoolean(False,False,False) # Team And Star Player Type
                else:
                    self.writeBoolean(False,True,False) # Team And Star Player Type
            else:
                if BotTeam[PlayerIndex] == 0:
                    self.writeBoolean(False,True,False) # Team And Star Player Type
                else:
                    self.writeBoolean(False,False,False) # Team And Star Player Type
            self.writeDataReference(16, BotBrawler[PlayerIndex]) # Player Brawler
            self.writeDataReference(29, -1) # Player Skin
            self.writeVInt(0) # Brawler Trophies
            self.writeVInt(1) # Brawler Power Level
            self.writeBoolean(False) # IsPlayer Array
            # Player Display Data
            self.writeString(BotName[PlayerIndex]) # Player Name
            self.writeVInt(100)
            self.writeVInt(28000000) # Player Profile Icon
            self.writeVInt(43000000) # Player Name Color
            # Player Display Data End
        # Player Entry Array End
        
        
        # Experience Entry Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(0) # Normal Experience Gained
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(0) # Star Player Experience Gained
        # Experience Entry Array End


        # Milestone Rewards Array
        self.writeVInt(0) # Milestones Count
        for x in range(0):
            self.writeDataReference(39, 0) # Milestones Index
        # Milestone Rewards Array End


        # Milestone Progress Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Milestone ID
        self.writeVInt(0) # Brawler Trophies
        self.writeVInt(0) # Brawler Highest Trophies
        self.writeVInt(5) # Milestone ID
        self.writeVInt(0) # Player Experience Points
        self.writeVInt(0) # Player Experience Points
        # Milestone Progress Array End
        
        
        self.writeDataReference(28, 0)  # Player Profile Icon
        

        self.writeBoolean(False) # Play Again 