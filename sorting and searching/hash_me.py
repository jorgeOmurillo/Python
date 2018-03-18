class HashTable:
    def __init__(self):
        self.size = 11
        self.data = [None] * self.size
        self.slots = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data     # replace data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.slots[data] = data
                else:
                    self.data[nextslot] = data  # replace data

            if self.slots[nextslot] == None:
                self.slots[nextslot] = key
                self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == startslot:
                    stop = True

        return data

    def delete(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                self.data[position] = None
            else:
                position = self.rehash(position, len(self.slots))

                if position == startslot:
                    stop = True

        return found

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = HashTable()
H[4] = "jorge"
H[11] = "ana"
H[1231] = "celular"

print(H.slots)
print(H.data)

H.delete(11)
print(H.slots)
print(H.data)
