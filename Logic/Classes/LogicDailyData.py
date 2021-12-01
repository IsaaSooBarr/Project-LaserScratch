from Logic.Classes.LogicOfferBundle import LogicOfferBundle
from Logic.Entry.AdStatus import AdStatus
from Logic.Entry.IntValueEntry import IntValueEntryLogicDailyData
from Logic.Entry.CooldownEntry import CooldownEntry
from Utility.ByteStream import Writer
from Utility.Utils import Utils


class LogicDailyData(Writer):
    def encode(self):
        self.writeVInt(Utils.getCurrentDate(self)) # Current Year and Day
        self.writeVInt(Utils.getTimeForNextDay(self)) # Time Remaining For Next Day
        self.writeVInt(0) # Player Trophies
        self.writeVInt(0) # Player Highest Trophies
        self.writeVInt(0) # Player Daily Highest Trophies
        self.writeVInt(1) # Collected Trophy Road Reward
        self.writeVInt(0) # Player Experience Points
        self.writeDataReference(28, 0) # Player Profile Icon
        self.writeDataReference(43, 0) # Player Name Color
        self.writeArrayVInt([]) # Played Game Modes


        # Selected Skins Array
        SelectedSkins = []
        self.writeVInt(len(SelectedSkins)) # Skins Count
        for i in range(len(SelectedSkins)):
            self.writeDataReference(29, i) # Selected Skin
        # Selected Skins Array End


        # Unlocked Skins Array
        UnlockedSkins = []
        self.writeVInt(len(UnlockedSkins)) # Skins Count
        for i in range(len(UnlockedSkins)):
            self.writeDataReference(29, i) # Unlocked Skin
        # Unlocked Skins Array End


        self.writeVInt(0) # Leaderboard Region
        self.writeVInt(0) # Player Highest League Trophies
        self.writeVInt(0) # Tokens Used In Battles
        self.writeBoolean(False) # Token Limit Reached State
        self.writeVInt(1) # Control Mode
        self.writeBoolean(True) # Battle Hints
        self.writeVInt(0) # Tokens Remaining From Token Doubler
        self.writeVInt(0) # Season End Timer
        self.writeBoolean(False, False, False, True) # Shop Exclusive Offer and Token Doubler State
        self.writeVInt(0) # Token Doubler Seem State
        self.writeVInt(0) # Event Tickets Seem State
        self.writeVInt(0) # Coin Packs Seem State
        self.writeVInt(0) # Change Name Cost
        self.writeVInt(0) # Timer For the Next Name Change


        # Shop Offers Array
        LogicOfferBundle.encode(self)
        # Shop Offers Array End


        # Brawl Box Ad Status Array
        AdStatus.encode(self)
        # Brawl Box Ad Status Array End
            
            
        self.writeVInt(0) # Available Tokens From Battles
        self.writeVInt(0) # Timer For New Tokens
        self.writeArrayVInt([]) # Event Tickets Purchased Index
        self.writeVInt(0) # Player Event Tickets
        self.writeVInt(0)
        self.writeDataReference(16, 0) # Selected Brawler
        self.writeString("BR") # Player Location
        self.writeString() # Supported Content Creator
        
        
        # Home Events Array
        IntValueEntryLogicDailyData.encode(self)
        # Home Events Array End


        # Cooldown Entry Array
        CooldownEntry.encode(self)
        # Cooldown Entry Array End 