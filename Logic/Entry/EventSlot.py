from Utility.ByteStream import Writer


class EventSlot(Writer):
    def encode(self):
        self.writeVInt(7) # Event Slots Count
        self.writeVInt(1) # Gem Grab 
        self.writeVInt(2) # Showdown
        self.writeVInt(3) # Daily Events
        self.writeVInt(4) # Special Events
        self.writeVInt(5) # Duo Showdown
        self.writeVInt(6) # Special Events (Duo Showdown)
        self.writeVInt(7) # Ticketed Events