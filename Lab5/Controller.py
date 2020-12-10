from model.Parser import Parser
from model.Scanner import Scanner


class Controller:
    def __init__(self):
        self.scanner = Scanner("input/p1.txt")
        self.parser = Parser("g2.txt")
        self.parser.populateParseTable()

    def parseResult(self, w):
        status, errorIndex = self.parser.parse(w)
        if status:
            print("Sequence " + str(w) + " is accepted")
            print("Pi: " + str(self.parser.pi))
            print("Derivation String: " + self.derivationString())
        else:
            print("Sequence " + str(w) + " is not accepted")
            print("Pi: " + str(self.parser.pi))
            print("Error at position: " + str(errorIndex) + " token: " + str(w[errorIndex]))

    def derivationString(self):
        str_builder = ""
        lastT = ""
        for index in self.parser.pi:
            if index == "epsilon":
                lastT = self.parser.grammar.getStartingSymbol()
                str_builder += lastT + "->"
                continue

            for key, value in self.parser.numberedProductions.items():
                if index == str(value):
                    x = ""
                    for i in key[1]:
                        x += i + " "
                    if x == "epsilon":
                        x = ""
                    lastT = lastT.replace(str(key[0]), str(x), 1)
                    str_builder += lastT + "->"

        return str_builder[0:-2]

    def scanSourceCode(self):
        self.scanner.lexicalAnalysis()
        self.scanner.writePIF()
        lexicalErrors = self.scanner.errors
        if len(lexicalErrors) == 0:
            pif = self.scanner.getPIF()
            print("First: " + str(self.parser.firstSet))
            print("Follow: " + str(self.parser.followSet))
            print("Numbered productions: ", str(self.parser.numberedProductions))
            print("Parse table: " + str(self.parser.parseTable))
            w = []
            for entry in pif.get():
                w.append(entry[0])

            self.parseResult(w)
