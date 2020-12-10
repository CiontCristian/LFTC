
class ProgramInternalForm:
    def __init__(self):
        self._pif = []

    def add(self, token, pos):
        self._pif.append((token, pos))

    def get(self):
        return self._pif

    def __str__(self):
        return str(self._pif)