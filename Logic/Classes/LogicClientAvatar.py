from Logic.Classes.LogicDataSlot import LogicDataSlotHeroOrItemUnlocked
from Logic.Classes.LogicDataSlot import LogicDataSlotHeroScore
from Logic.Classes.LogicDataSlot import LogicDataSlotHeroHighestScore
from Logic.Classes.LogicDataSlot import LogicDataSlotResourceCount
from Logic.Classes.LogicDataSlot import LogicDataSlotHeroPower
from Logic.Classes.LogicDataSlot import LogicDataSlotHeroLevel
from Logic.Classes.LogicDataSlot import LogicDataSlotCardCount
from Logic.Classes.LogicDataSlot import LogicDataSlotHeroSeenState
from Utility.ByteStream import Writer


class LogicClientAvatar(Writer):
    def encode(self):
        self.writeLogicLong(0, 1) # Account ID
        self.writeLogicLong(0, 0)
        self.writeLogicLong(0, 0)
        self.writeStringReference("Brawler") # Player Name
        self.writeBoolean(True) # Registered Name State
        self.writeInt(-1)
        self.writeVInt(8) # Commodity Count


        # Unlocked Brawlers and Resources Array
        LogicDataSlotHeroOrItemUnlocked.encode(self)
        # Unlocked Brawlers and Resources Array End


        # Brawlers Trophies Array
        LogicDataSlotHeroScore.encode(self)
        # Brawlers Trophies Array End


        # Brawlers Highest Trophies Array
        LogicDataSlotHeroHighestScore.encode(self)
        # Brawlers Highest Trophies Array End
        
        
        # Highest Resources Amount Array
        LogicDataSlotResourceCount.encode(self)
        # Highest Resources Amount Array End


        # Brawlers Power Points Array
        LogicDataSlotHeroPower.encode(self)
        # Brawlers Power Points Array End


        # Brawlers Power Level Array
        LogicDataSlotHeroLevel.encode(self)
        # Brawlers Power Level Array End


        # Brawlers Star Powers Array
        LogicDataSlotCardCount.encode(self)
        # Brawlers Star Powers Array End
        
        
        # Brawlers Seem State Array
        LogicDataSlotHeroSeenState.encode(self)
        # Brawlers Seem State Array End

        
        self.writeVInt(0) # Player Gems
        self.writeVInt(0) # Player Free Gems
        self.writeVInt(1) # Player Experience Level
        self.writeVInt(100)
        self.writeVInt(0) # Cumulative Purchased Gems
        self.writeVInt(0) # Battles Count
        self.writeVInt(0) # Win Count
        self.writeVInt(0) # Lose Count
        self.writeVInt(0) # Win/Loose Streak
        self.writeVInt(0) # Npc Win Count
        self.writeVInt(0) # Npc Lose Count
        self.writeVInt(2) # Tutorial State