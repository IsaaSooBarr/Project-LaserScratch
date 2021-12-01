from Packets.Messages.Server.Login.LoginOkMessage import LoginOkMessage
from Packets.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Packets.Messages.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Packets.Messages.Server.Alliance.AllianceWarMessage import AllianceWarMessage
from Utility.ByteStream import Reader


class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.high_id = self.readInt()
        self.player.low_id = self.readInt()
        self.player.token = self.readString()
        self.player.Major = self.readInt()
        self.player.Revision = self.readInt()
        self.player.Minor = self.readInt()
        self.FingerprintSHA = self.readString()
        

    def process(self):
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player).send()
        AllianceWarMessage(self.client, self.player).send()