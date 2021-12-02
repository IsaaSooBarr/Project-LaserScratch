from Utility.ByteStream import Writer
from Utility.Utils import Utils


class LobbyInfoMessage(Writer):
    def __init__(self, client, player, count):
        super().__init__(client)
        self.id = 23457
        self.client = client
        self.player = player
        self.count = count


    def encode(self):
        self.writeVInt(self.count) # Players Online
        self.writeString(f"Project LaserScratch (v1.1.1)\nVersion: {self.player.Major}.{self.player.Minor}.{self.player.Revision}\n{Utils.getLobbyInfoCurrentDate(self)}")
        
        
        # Lobby Info Entry Array
        self.writeVInt(0) # Events Count
        for x in range(0):
            self.writeVInt(0) # Event Index
            self.writeVInt(0) # Pvp Battle
            self.writeVInt(0) # Pvp Matchmake
            self.writeVInt(0) # Co-op Battle
            self.writeVInt(0) # Co-op Matchmake
        # Lobby Info Entry Array End
        
