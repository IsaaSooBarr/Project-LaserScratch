from io import BufferedReader, BytesIO
import zlib


class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''


    def writeInt(self, data, length = 4):
        self.buffer += data.to_bytes(length, self.endian, signed=True)
        

    def writeIntLE(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')


    def writeUInteger(self, integer: int, length: int = 1):
        self.buffer += integer.to_bytes(length, self.endian, signed=False)


    def writeLong(self, x, y):
        self.writeInt(x)
        self.writeInt(y)


    def writeLogicLong(self, x, y):
        self.writeVInt(x)
        self.writeVInt(y)


    def writeArrayVInt(self, data):
        if len(data) >= 1:
            self.writeVInt(len(data))
            for x in data:
                self.writeVInt(x)
        else:
            self.writeVInt(0)


    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)


    def writeInt8(self, integer: int):
        self.writeInt(integer, 1)


    def writeInt16(self, data):
        self.writeInt(data, 2)


    def writeBoolean(self, *args):
        boolean = 0
        i = 0
        for value in args:
            if value:
                boolean |= 1 << i
            i += 1
        self.writeByte(boolean)


    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))
            

    def writeVInt(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        elif data < 0:
            self.writeVInt((2147483648 * 2) + data)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        self.buffer += final


    def writeDataReference(self, x, y=0):
        if x >= 1 and y >= 0:
            self.writeVInt(x)
            self.writeVInt(y)
        else:
            self.writeVInt(0)


    def writeString(self, string: str = None):
        if string is None:
            self.writeInt(-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded


    def writeStringShort(self, string: str = None):
        if string is None:
            self.writeInt(-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt8(len(encoded))
            self.buffer += encoded


    def writeStringReference(self, string: str = None):
        if string is None:
            self.writeInt(-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded
        
        
    def writeCompressedString(self, data: bytes):
        compressed = zlib.compress(data)
        self.writeInt(len(compressed) + 4)
        self.writeIntLE(len(data))
        self.buffer += compressed


    def writeByte(self, data):
        self.buffer += data.to_bytes(1, 'big', signed=False)


    def size(self):
        return len(self.buffer)


    def getRaw(self):
        return self.buffer


    def writeBytes(self, data):
        self.buffer += data


    def ChronosTextEntry(self, TextType, TextEntry):
        self.writeInt(TextType)
        self.writeStringReference(TextEntry)


    def ChronosFileEntry(self, FilePath, FileSHA):
        self.writeStringReference(FilePath)
        self.writeStringReference(FileSHA)


    def send(self):
        self.encode()
        packet = self.buffer
        self.buffer = self.id.to_bytes(2, 'big', signed=True)
        self.writeInt(len(packet), 3)
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
        self.client.send(self.buffer)
        print(f'[INFO] Packet {self.id}: {self.__class__.__name__} was sent!')


class Reader(BufferedReader):
    def __init__(self, initial_bytes, endian: str = 'big'):
        super().__init__(BytesIO(initial_bytes))
        self.buffer = initial_bytes
        self.endian = endian
        self.i = 0


    def readByte(self):
        return int.from_bytes(self.read(1), "big")


    def readVInt(self):
        n = self.readVarint(True)
        return (n >> 1) ^ (-(n & 1))


    def readShort(self, length=2):
        return int.from_bytes(self.read(length), "big")


    def readInt(self, length=4):
        return int.from_bytes(self.read(length), "big")


    def readLong(self):
        x = self.readInt()
        y = self.readInt()
        return x, y


    def readUInt8(self) -> int:
        return self.readUInteger()*64


    def readUInteger(self, length: int = 1) -> int:
        result = 0
        for x in range(length):
            byte = self.buffer[self.i]
            bit_padding = x * 8
            if self.endian == 'big':
                bit_padding = (8 * (length - 1)) - bit_padding
            result |= byte << bit_padding
            self.i += 1
        return result


    def readVarint(self, rotate: bool = True):
        result = 0
        shift = 0
        while True:
            byte = self.readByte()
            if rotate and shift == 0:
                seventh = (byte & 0x40) >> 6
                msb = (byte & 0x80) >> 7
                n = byte << 1
                n = n & ~0x181
                byte = n | (msb << 7) | seventh
            result |= (byte & 0x7f) << shift
            shift += 7
            if not (byte & 0x80):
                break
        return result


    def readBoolean(self) -> bool:
        if self.readByte() >= 1:
            return True
        else:
            return False


    def readDataReference(self):
        a = self.readVInt()
        if a != 0:
            b = self.readVInt()
        else:
            b = -1
        return a, b


    def readString(self):
        length = self.readInt()
        if length == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(length)
            except MemoryError:
                raise IndexError("String out of range!")
            else:
                return decoded.decode('utf-8')


    def peekInt(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")


    def readLogicLong(self):
        x = self.readVInt()
        y = self.readVInt()
        return x, y