from Utility.ByteStream import Writer


class CooldownEntry(Writer):
    def encode(self):
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(0, 0)
            self.writeVInt(0)