from Utility.ByteStream import Writer


class RelaseEntry(Writer):
    def encode(self):
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeDataReference(16, 0) # Locked Item
            self.writeInt(0) # Locked Timer
            self.writeInt(-1)