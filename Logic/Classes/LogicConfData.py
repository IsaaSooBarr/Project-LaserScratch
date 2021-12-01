from Logic.Entry.EventSlot import EventSlot
from Logic.Entry.EventData import EventDataActiveEvent
from Logic.Entry.EventData import EventDataUpcomingEvent
from Logic.Entry.RelaseEntry import RelaseEntry
from Logic.Entry.IntValueEntry import IntValueEntryLogicConfData
from Utility.ByteStream import Writer
from Utility.Utils import Utils


class LogicConfData(Writer):
    def encode(self):
        self.writeVInt(Utils.getCurrentDate(self)) # Current Year and Day
        self.writeVInt(100) # Brawl Box Tokens
        self.writeVInt(10) # Shop Brawl Box Cost
        self.writeVInt(30) # Shop Big Box Cost
        self.writeVInt(3) # Shop Big Box Multipler
        self.writeVInt(80) # Shop Megabox Cost
        self.writeVInt(10) # Shop Megabox Multipler
        self.writeVInt(50) # Shop Token Doubler Cost
        self.writeVInt(1000) # Shop Token Doubler Amount
        self.writeVInt(550) # Minimum Brawler Trophies For Season Reset
        self.writeVInt(50) # Brawler Trophy Loss Percentage In Season Reset
        self.writeVInt(999900) # Token Limit Amount
        self.writeArrayVInt([0,30,80,170,350,0]) # Boxes With Guaranteed Brawlers Cost
        
        
        # Event Slots Array
        EventSlot.encode(self)
        # Event Slots Array End
        
        
        # Event Slots Data Array
        EventDataActiveEvent.encode(self)
        # Event Slots Data Array End
        
        
        # Upcoming Event Slots Data Array
        EventDataUpcomingEvent.encode(self)
        # Upcoming Event Slots Data Array End
        
        
        self.writeArrayVInt([20,35,75,140,290,480,800,1250]) # Brawler Coins Upgrade Cost
        self.writeArrayVInt([1,2,3,4,5,10,15,20]) # Highstakes Rewards
        self.writeArrayVInt([10,30,80]) # Event Tickets Cost
        self.writeArrayVInt([6,20,60]) # Event Tickets Amount
        self.writeArrayVInt([20,50,140,280]) # Coin Packs Cost
        self.writeArrayVInt([150,400,1200,2600]) # Coin Packs Amount
        self.writeVInt(0) # Coin Packs State
        self.writeVInt(200) # Maximun Battle Tokens
        self.writeVInt(20) # Tokens Gained In Refresh
        self.writeVInt(8640) # Tokens Refresh Timer
        self.writeVInt(10) # Big Box Star Tokens
        self.writeVInt(5)
        self.writeBoolean(False,False,False) # Unlocked Event Slots State
        self.writeVInt(50)
        self.writeVInt(604800)
        self.writeBoolean(True) # Shop Boxes Enabled State


        # Locked For Chronos Array
        RelaseEntry.encode(self)
        # Locked For Chronos Array End
        
        
        # Home Events Array
        IntValueEntryLogicConfData.encode(self)
        # Home Events Array End