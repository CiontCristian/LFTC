from SymbolTable import SymbolTable
from ProgramInternalForm import ProgramInternalForm
import re

pif = ProgramInternalForm()
st = SymbolTable(11)

codification = {}
operators = []
separators = []
reserved = []
fileName = "input/p1.txt"


def isOperator(token):
    return token in operators


def isSeparator(token):
    return token in separators


def isReserved(token):
    return token in reserved


def isIdentifier(token):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,8}$', token) is not None and re.match('^true|false$', token) is None


def isConstant(token):
    return re.match(r'^(0|[+-]?[1-9][0-9]*|true|false)$', token) is not None


def findToken(token):
    return codification[token]


def getLanguageSpecs():
    fileNameLanguageSpecs = "input/token.in"
    cnt = 0
    with open(file=fileNameLanguageSpecs) as file:
        for line in file:
            line = line.strip().split(' ')
            if len(line) == 1:
                codification[' '] = int(line[0])
            else:
                codification[line[1]] = int(line[0])

            if 1 < cnt < 17:
                operators.append(line[1])
            elif 17 <= cnt < 26:
                if len(line) == 1:
                    separators.append(' ')
                else:
                    separators.append(line[1])
            elif 26 <= cnt < 37:
                reserved.append(line[1])

            cnt += 1


def writeST():
    with open("output/st.out", 'w') as file:
        file.write("The data structure used is a hashtable")
        file.write("\n")
        file.write(str(st))


def writePIF():
    with open("output/pif.out", 'w') as file:
        file.write(str(pif))


def tokenize():
    getLanguageSpecs()
    result = []
    with open(fileName) as file:
        for line in file:
            line = line.strip()
            line = re.split('(\[|\]|\{|\}|\(|\)|;|,| |:=|==|<>|<|<=|>|>=|\+|\-|\*|div|mod|and|or|not)', line)
            result.append(line)

    return result


def lexicalAnalysis():
    current_program = tokenize()
    current_line = 0
    try:
        for line in current_program:
            current_line += 1
            print(line)
            for token in line:
                if token == '' or token == ' ':
                    continue
                else:
                    if isSeparator(token):
                        print(token + " is a separator")
                        pif.add(codification[token], -1)
                    elif isOperator(token):
                        print(token + " is an operator")
                        pif.add(codification[token], -1)
                    elif isReserved(token):
                        print(token + " is a reserved word")
                        pif.add(codification[token], -1)
                    elif isIdentifier(token):
                        print(token + " is an identifier")
                        pos = st.add(token)
                        pif.add(codification['identifier'], pos)
                    elif isConstant(token):
                        print(token + " is a constant")
                        pos = st.add(token)
                        pif.add(codification['constant'], pos)
                    else:
                        raise Exception("Lexical error at line " + str(current_line) + " " + str(line))
        print("Program is lexically correct!")
    except Exception as e:
        print(e)


lexicalAnalysis()
writeST()
writePIF()

