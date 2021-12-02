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
        Unknown1 = self.readString()
        self.DeviceID = self.readString()
        Unknown2 = self.readString()
        self.Device = self.readString()
        self.PreferredLanguage = self.readDataReference()[1]
        self.PreferredDeviceLanguage = self.readString()
        self.DeviceUUID = self.readString()
        self.OSVersion = self.readString()
        self.isAndroid = self.readBoolean()
        Unknown3 = self.readStringReference()
        self.AndroidID = self.readStringReference()
        Unknown4 = self.readStringReference()
        self.isAdvertisingEnabled = self.readBoolean()
        Unknown5 = self.readString()
        Unknown6 = self.readInt()
        self.AppStore = self.readVInt()
        Unknown7 = self.readStringReference()
        Unknown8 = self.readStringReference()
        self.AppVersion = self.readStringReference()
        Unknown9 = self.readStringReference()
        Unknown10 = self.readStringReference()
        self.TencentPlatform = self.readVInt()
        Unknown11 = self.readStringReference()
        Unknown12 = self.readStringReference()
        Unknown13 = self.readStringReference()
        print("Account HighID:", self.player.high_id)
        print("Account LowID:", self.player.low_id)
        print("Pass Token:", self.player.token)
        print("Client Major:", self.player.Major)
        print("Client Content:", self.player.Revision)
        print("Client Build:", self.player.Minor)
        print("Resource SHA:", self.FingerprintSHA)
        print("Unknown:", Unknown1)
        print("Device ID:", self.DeviceID)
        print("Unknown:", Unknown2)
        print("Device Model:", self.Device)
        print("App Language:", self.PreferredLanguage)
        print("Device Language:", self.PreferredDeviceLanguage)
        print("Device UUID:", self.DeviceUUID)
        print("OS Version:", self.OSVersion)
        print("isAndroid:", self.isAndroid)
        print("Unknown:", Unknown3)
        print("Android ID:", self.AndroidID)
        print("Unknown:", Unknown4)
        print("Advertising Enabled:", self.isAdvertisingEnabled)
        print("Unknown:", Unknown5)
        print("Unknown:", Unknown6)
        print("App Store Type:", self.AppStore)
        print("Unknown:", Unknown7)
        print("Unknown:", Unknown8)
        print("App Version:", self.AppVersion)
        print("Unknown:", Unknown9)
        print("Unknown:", Unknown10)
        print("Tencent Platform:", self.TencentPlatform)
        print("Unknown:", Unknown11)
        print("Unknown:", Unknown12)
        print("Unknown:", Unknown13)
        

    def process(self):
        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()
        MyAllianceMessage(self.client, self.player).send()
        AllianceWarMessage(self.client, self.player).send()