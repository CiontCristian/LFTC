class ParseTable:
    def __init__(self):
        self.table = {}

    def put(self, key, value):
        self.table[key] = value

    def getKeyValue(self, key):
        #values = []
        #index = -1
        for currentKey in self.table.keys():
            currentValue = self.table[currentKey]
            if currentKey == key:
                #index = currentValue[1]
                #values.append(currentValue[0])
                return currentValue

        return None
        #return values, index

    def containsKey(self, key):
        return key in self.table.keys()

    def __str__(self):
        str_builder = ""
        for currentKey in self.table.keys():
            currentValue = self.table[currentKey]
            x = ""
            for i in currentValue[0]:
                x += i
            str_builder += "M[" + str(currentKey[0]) + "," + str(currentKey[1]) + "] = [" + str(x) + "," + str(currentValue[
                1]) + "]\n"

        return str_builder
