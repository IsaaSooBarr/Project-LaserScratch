from Packets.Messages.Server.Battle.BattleEndMessage import BattleEndMessage
from Utility.ByteStream import Reader


class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.BattleResult = self.readVInt()
        self.readVInt()
        self.player.Rank = self.readVInt()
        self.Map = self.readDataReference()[1]  # Locations CsvID
        self.BattlePlayers = self.readVInt() # Battle End Players
        
        
        self.player.BrawlerID = self.readDataReference()[1] 
        self.player.SkinID = self.readDataReference()[1] 
        self.PlayerTeam = self.readVInt() 
        self.IsPlayer = self.readBoolean()
        self.PlayerName = self.readString() 


        self.Bot1Brawler = self.readDataReference()[1] 
        self.Bot1Skin = self.readDataReference()[1]
        self.Bot1Team = self.readVInt() 
        self.Bot1IsPlayer = self.readBoolean()
        self.Bot1Name = self.readString()


        self.Bot2Brawler = self.readDataReference()[1]
        self.Bot2Skin = self.readDataReference()[1]
        self.Bot2Team = self.readVInt() 
        self.Bot2IsPlayer = self.readBoolean()
        self.Bot2Name = self.readString()


        self.Bot3Brawler = self.readDataReference()[1]
        self.Bot3Skin = self.readDataReference()[1]
        self.Bot3Team = self.readVInt() 
        self.Bot3IsPlayer = self.readBoolean()
        self.Bot3Name = self.readString()


        self.Bot4Brawler = self.readDataReference()[1]
        self.Bot4Skin = self.readDataReference()[1]
        self.Bot4Team = self.readVInt() 
        self.Bot4IsPlayer = self.readBoolean()
        self.Bot4Name = self.readString()


        self.Bot5Brawler = self.readDataReference()[1]
        self.Bot5Skin = self.readDataReference()[1]
        self.Bot5Team = self.readVInt() 
        self.Bot5IsPlayer = self.readBoolean()
        self.Bot5Name = self.readString()
        
        
        self.Bot6Brawler = self.readDataReference()[1]
        self.Bot6Skin = self.readDataReference()[1]
        self.Bot6Team = self.readVInt() 
        self.Bot6IsPlayer = self.readBoolean()
        self.Bot6Name = self.readString()
        
        
        self.Bot7Brawler = self.readDataReference()[1]
        self.Bot7Skin = self.readDataReference()[1]
        self.Bot7Team = self.readVInt() 
        self.Bot7IsPlayer = self.readBoolean()
        self.Bot7Name = self.readString()
        
        
        self.Bot8Brawler = self.readDataReference()[1]
        self.Bot8Skin = self.readDataReference()[1]
        self.Bot8Team = self.readVInt() 
        self.Bot8IsPlayer = self.readBoolean()
        self.Bot8Name = self.readString()
        
        
        self.Bot9Brawler = self.readDataReference()[1]
        self.Bot9Skin = self.readDataReference()[1]
        self.Bot9Team = self.readVInt() 
        self.Bot9IsPlayer = self.readBoolean()
        self.Bot9Name = self.readString()
        
        
    def process(self):
         self.player.Bot1Name = self.Bot1Name
         self.player.Bot2Name = self.Bot2Name
         self.player.Bot3Name = self.Bot3Name
         self.player.Bot4Name = self.Bot4Name
         self.player.Bot5Name = self.Bot5Name
         self.player.Bot6Name = self.Bot6Name
         self.player.Bot7Name = self.Bot7Name
         self.player.Bot8Name = self.Bot8Name
         self.player.Bot9Name = self.Bot9Name
         self.player.Bot1Brawler = self.Bot1Brawler
         self.player.Bot2Brawler = self.Bot2Brawler
         self.player.Bot3Brawler = self.Bot3Brawler
         self.player.Bot4Brawler = self.Bot4Brawler
         self.player.Bot5Brawler = self.Bot5Brawler
         self.player.Bot6Brawler = self.Bot6Brawler
         self.player.Bot7Brawler = self.Bot7Brawler
         self.player.Bot8Brawler = self.Bot8Brawler
         self.player.Bot9Brawler = self.Bot9Brawler
         self.player.PlayerTeam = self.PlayerTeam
         self.player.Bot1Team = self.Bot1Team
         self.player.Bot2Team = self.Bot2Team
         self.player.Bot3Team = self.Bot3Team
         self.player.Bot4Team = self.Bot4Team
         self.player.Bot5Team = self.Bot5Team
         self.player.Bot6Team = self.Bot6Team
         self.player.Bot7Team = self.Bot7Team
         self.player.Bot8Team = self.Bot8Team
         self.player.Bot9Team = self.Bot9Team
         self.player.BattlePlayers = self.BattlePlayers
         if self.BattlePlayers == 10 and self.Bot1Team == 0:
             self.Type = 5
         elif self.BattlePlayers == 10:
             self.Type = 2
         elif self.BattlePlayers == 3 and self.Map in [27, 29, 39, 68]:
             self.Type = 3
         elif self.BattlePlayers == 3 and self.Map in [57, 67, 133, 269]:
             self.Type = 6
         elif self.BattlePlayers == 6 and self.Map in [21, 30, 65, 66, 119, 120]:
             self.Type = 4
         else:
             self.Type = 1
         BattleEndMessage(self.client, self.player, self.Type).send()