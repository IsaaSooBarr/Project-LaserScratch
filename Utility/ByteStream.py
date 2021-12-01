from io import BufferedReader, BytesIO
import zlib


class Writer:
    def __init__(self, client, endian: str = 'big'):
        self.client = client
        self.endian = endian
        self.buffer = b''


    def writeInt(self, data: int, length: int = 4):
        if data > 0:
            self.buffer += data.to_bytes(length, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(length, 'big', signed=True)


    def writeInt8(self, data):
        self.writeInt(data, 1)


    def writeInt16(self, data):
        self.writeInt(data, 2)


    def writeInt24(self, data):
        self.writeInt(data, 3)


    def writeIntLE(self, data, length=4):
        self.buffer += data.to_bytes(length, 'little')


    def writeLong(self, high, low):
        self.buffer += high.to_bytes(4, 'big') + low.to_bytes(4, 'big')


    def writeUInteger(self, data: int, length: int = 1):
        self.buffer += data.to_bytes(length, 'big', signed=False)


    def writeUInt8(self, integer: int):
        self.writeUInteger(integer)
        

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


    def writeArrayVInt(self, arraydata):
        self.writeVInt(len(arraydata))
        for i in arraydata:
            self.writeVInt(i)


    def writeLogicLong(self, high, low):
        self.writeVInt(high)
        self.writeVInt(low)


    def writeDataReference(self, ClassID, InstanceID=0):
        if ClassID >= 1 and InstanceID >= 0:
            self.writeVInt(ClassID)
            self.writeVInt(InstanceID)
        else:
            self.writeVInt(0)


    def writeBoolean(self, *args):
        boolean = 0
        i = 0
        for value in args:
            if value:
                boolean |= 1 << i
            i += 1
        self.writeByte(boolean)


    def writeString(self, string = None):
        if string is None:
            self.writeInt((2 ** 32) - 1)
        else:
            if type(string) == bytes:
                encoded = string
            else:
                encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            self.buffer += encoded


    def writeStringReference(self, string = None):
        if string is None:
            self.writeInt((2 ** 32) - 1)
        else:
            if type(string) == bytes:
                encoded = string
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
        if data > 255:
            self.buffer += data.to_bytes(2, 'big', signed=False)
        elif data > 127:
            self.buffer += data.to_bytes(1, 'big', signed=False)
        else:
            self.buffer += data.to_bytes(1, 'big', signed=True)


    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            self.buffer += bytes.fromhex(''.join(data.split()).replace('-', ''))


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
        self.writeInt24(len(packet))
        if hasattr(self, 'version'):
            self.writeInt16(self.version)
        else:
            self.writeInt16(0)
        self.buffer += packet + b'\xff\xff\x00\x00\x00\x00\x00'
        self.client.send(self.buffer)
        print(f'[INFO] Packet {self.id}: {self.__class__.__name__} was sent!')


class Reader(BufferedReader):
    def __init__(self, header_bytes):
        super().__init__(BytesIO(header_bytes))
        self.bytes_of_packets = header_bytes


    def readInt(self):
        return int.from_bytes(self.read(4), "big")


    def readInt8(self):
        return int.from_bytes(self.read(1), "big")


    def readInt16(self):
        return int.from_bytes(self.read(2), "big")


    def readInt24(self):
        return int.from_bytes(self.read(3), "big")


    def readIntLE(self):
        return int.from_bytes(self.read(4), "little")


    def readLong(self):
        high = self.readInt()
        low = self.readInt()
        return high, low


    def readUInteger(self, length: int = 1, endian: str = 'big'):
        result = 0
        i = 0
        for x in range(length):
            byte = self.bytes_of_packets[i]
            bit_padding = x * 8
            if endian == 'big':
                bit_padding = (8 * (length - 1)) - bit_padding
            result |= byte << bit_padding
            i += 1
        return result


    def readUInt8(self):
        return self.readUInteger()


    def readVInt(self):
        n = self.readVarInt(True)
        return (n >> 1) ^ (-(n & 1))


    def readLogicLong(self):
        high = self.readVInt()
        low = self.readVInt()
        return high, low


    def readDataReference(self):
        ClassID = self.readVInt()
        if ClassID != 0:
            InstanceID = self.readVInt()
        else:
            InstanceID = -1
        return ClassID, InstanceID


    def readBoolean(self):
        result = bool.from_bytes(bytes=self.read(1), byteorder='big', signed=False)
        if result == True:
            return True
        else:
            return False


    def readString(self):
        lenght = self.readInt()
        if lenght == pow(2, 32) - 1:
            return b""
        else:
            try:
                decoded = self.read(lenght)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')


    def readStringReference(self):
        return self.readString()


    def readCompressedString(self):
        self.readInt()
        data_length = self.readIntLE()
        compressed = self.readBytes(data_length)
        return zlib.decompress(compressed)


    def readByte(self):
        return int.from_bytes(self.read(1), "big")


    def readBytes(self, length):
        return self.read(length)


    def readShort(self, length=2):
        return int.from_bytes(self.read(length), "big")


    def readVarInt(self, rotate: bool = True):
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


    def peekInt(self, length=4):
        return int.from_bytes(self.peek(length)[:length], "big")