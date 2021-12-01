from Logic.Classes.LogicClientHome import LogicClientHome
from Logic.Classes.LogicClientAvatar import LogicClientAvatar
from Utility.ByteStream import Writer
from Utility.Utils import Utils


class OwnHomeDataMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.client = client
        self.player = player


    def encode(self):
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)
        self.writeVInt(Utils.getCurrentTimeInSecondsSinceEpoch(self)) # Current Time
        