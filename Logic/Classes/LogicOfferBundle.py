from Utility.ByteStream import Writer
from Utility.Utils import Utils


class LogicOfferBundle(Writer):
    def encode(self):
        self.writeVInt(0) # Shop Offers Count
        for x in range(0):
            self.writeVInt(0) # Offer Items Count
            for x in range(0):
                self.writeVInt(0) # Offer Item ID
                self.writeVInt(0) # Offer Amount
                self.writeDataReference(16, 0) # Offer Character
                self.writeVInt(0) # Offer Item Extra Data
            self.writeVInt(0) # Offer Resource Type
            self.writeVInt(0) # Offer Cost
            self.writeVInt(0) # Offer Timer
            self.writeVInt(0) # Offer New Tag State
            self.writeVInt(0) # Offer Bundle Percentage Value
            self.writeBoolean(False) # Offer Purchased
            self.writeVInt(0) 
            self.writeBoolean(False) # Daily Deals Offer
            self.writeVInt(0) # Offer Original Cost
            self.ChronosTextEntry(2, "") # Offer Text Entry
            self.writeBoolean(False)