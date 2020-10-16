class SymbolTable:
    def __init__(self, size):
        self._size = size
        self._hashTable = [[] for _ in range(self._size)]

    def __str__(self):
        return str(self._hashTable)

    def hash(self, varName):
        asciiSum = 0
        for letter in varName:
            asciiSum += ord(letter)

        return asciiSum % self._size

    def find(self, varName):
        pos = self.hash(varName)
        for elem in self._hashTable[pos]:
            if elem == varName:
                return pos
        return -1

    def add(self, varName):
        pos = self.hash(varName)
        if self.find(varName) == -1:
            self._hashTable[pos].append(varName)

        return pos


table = SymbolTable(7)
table.add('counter')
table.add('a')
table.add('b')
table.add('counter2')
table.add('27')
table.add('216')
table.add('True')
table.add('aaa')
print(table)
