import re
from model.ProgramInternalForm import ProgramInternalForm
from model.SymbolTable import SymbolTable


class Scanner:
    def __init__(self, fileName):
        self.pif = ProgramInternalForm()
        self.st = SymbolTable(11)
        self.codification = {}
        self.operators = []
        self.separators = []
        self.reserved = []
        self.fileName = fileName
        self.errors = []

    def getPIF(self):
        return self.pif

    def isOperator(self, token):
        return token in self.operators

    def isSeparator(self, token):
        return token in self.separators

    def isReserved(self, token):
        return token in self.reserved

    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,8}$', token) is not None and re.match('^true|false$',
                                                                                            token) is None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*|true|false)$', token) is not None

    def findToken(self, token):
        return self.codification[token]

    def getLanguageSpecs(self):
        fileNameLanguageSpecs = "input/token.in"
        cnt = 0
        with open(file=fileNameLanguageSpecs) as file:
            for line in file:
                line = line.strip().split(' ')
                if len(line) == 1:
                    self.codification[' '] = int(line[0])
                else:
                    self.codification[line[1]] = int(line[0])

                if 1 < cnt < 17:
                    self.operators.append(line[1])
                elif 17 <= cnt < 26:
                    if len(line) == 1:
                        self.separators.append(' ')
                    else:
                        self.separators.append(line[1])
                elif 26 <= cnt < 37:
                    self.reserved.append(line[1])

                cnt += 1

    def writeST(self):
        with open("output/st.out", 'w') as file:
            file.write("The data structure used is a hashtable")
            file.write("\n")
            file.write(str(self.st))

    def writePIF(self):
        with open("output/pif.out", 'w') as file:
            file.write(str(self.pif))

    def tokenizeByArithmeticOperators(self, line):
        return re.split('(\+|-|\*|div|mod|and|or|not)', line)

    def tokenize(self):
        self.getLanguageSpecs()
        result = []
        with open(self.fileName) as file:
            for line in file:
                line = line.strip()
                new_line = []
                line = re.split('(\[|\]|\{|\}|\(|\)|;|,| |:=|==|<>|<|<=|>|>=)', line)
                print(line)
                for i in range(len(line)):
                    if line[i] == '-0' or line[i] == '+0':
                        new_line.append(line[i])
                    elif line[i] not in self.separators + self.operators + self.reserved and not self.isConstant(
                            line[i]) and not self.isIdentifier(line[i]):
                        new_line.extend(self.tokenizeByArithmeticOperators(line[i]))

                    else:
                        new_line.append(line[i])
                result.append(new_line)

        return result

    def lexicalAnalysis(self):
        current_program = self.tokenize()
        current_line = 0
        try:
            for line in current_program:
                current_line += 1
                print(line)
                for token in line:
                    if token == '' or token == ' ':
                        continue
                    else:
                        if self.isSeparator(token):
                            print(token + " is a separator")
                            self.pif.add(self.codification[token], -1)
                        elif self.isOperator(token):
                            print(token + " is an operator")
                            self.pif.add(self.codification[token], -1)
                        elif self.isReserved(token):
                            print(token + " is a reserved word")
                            self.pif.add(self.codification[token], -1)
                        elif self.isIdentifier(token):
                            print(token + " is an identifier")
                            pos = self.st.add(token)
                            self.pif.add(self.codification['identifier'], pos)
                        elif self.isConstant(token):
                            print(token + " is a constant")
                            pos = self.st.add(token)
                            self.pif.add(self.codification['constant'], pos)
                        else:
                            self.errors.append("Lexical error at line " + str(current_line) + " " + str(
                                line) + " " + "at token: " + token)
                            raise Exception("Lexical error at line " + str(current_line) + " " + str(
                                line) + " " + "at token: " + token)
            print("Program is lexically correct!")
        except Exception as e:
            print(e)
