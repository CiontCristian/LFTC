from model.Grammar import Grammar
from model.ParseTable import ParseTable


class Parser:
    def __init__(self, fileName):
        self.grammar = Grammar.read(fileName)
        self.firstSet = {}
        self.followSet = {}
        self.populateFirstSet()
        self.populateFollowSet()
        self.numberedProductions = {}
        self.parseTable = ParseTable()
        self.alpha = []
        self.beta = []
        self.pi = []

    def populateFirstSet(self):
        for nonTerminal in self.grammar.getNonTerminals():
            self.firstSet[nonTerminal] = self.first(nonTerminal)

    def populateFollowSet(self):
        for nonTerminal in self.grammar.getNonTerminals():
            self.followSet[nonTerminal] = self.follow(nonTerminal)

    def first(self, nonTerminal):
        if nonTerminal in self.firstSet.keys():
            return self.firstSet[nonTerminal]

        terminals = self.grammar.getTerminals()
        result = []

        if nonTerminal in terminals:
            result.append(nonTerminal)
        elif nonTerminal == "epsilon":
            result.append(nonTerminal)
        else:
            for production in self.grammar.getProductionsForNonterminal(nonTerminal):
                for symbol in production:
                    firstOfSymbol = self.first(symbol)
                    result.extend(firstOfSymbol)
                    if "epsilon" not in firstOfSymbol:
                        break
        result = set(result)
        return result

    def allSymbolsAfterNonTerminal(self, prods, pos):
        result = []

        for i in range(len(prods)):
            if i > pos:
                result.append(prods[i])

        return result

    def follow(self, nonTerminal):
        if nonTerminal in self.followSet.keys():
            return self.followSet[nonTerminal]

        result = []

        if self.grammar.getStartingSymbol() == nonTerminal:
            result.append("$")

        for production in self.grammar.getProductionsContainingNonterminal(nonTerminal):

            firstSymbol = production[0]
            rules = production[1]
            pos = rules.index(nonTerminal)

            symbolsAfterNonTerminal = self.allSymbolsAfterNonTerminal(rules, pos)

            if not symbolsAfterNonTerminal and nonTerminal != firstSymbol:
                result.extend(self.follow(firstSymbol))
            else:
                for symbol in symbolsAfterNonTerminal:
                    firstOfSymbol = self.first(symbol)
                    if "epsilon" in firstOfSymbol:
                        temp = self.first(symbol)
                        temp = list(filter(lambda x: x != "epsilon", temp))
                        result.extend(temp)
                        result.extend(self.follow(firstSymbol))
                    else:
                        temp = self.first(symbol)
                        temp = list(filter(lambda x: x != "epsilon", temp))
                        result.extend(temp)

        result = set(result)
        return result

    def numberProductions(self):
        pos = 1
        for production in self.grammar.getProductions():
            startSymbol = production[0]
            rules = tuple(production[1])
            # for rule in production[1]:
            self.numberedProductions[(startSymbol, rules)] = pos
            pos += 1

    def populateParseTable(self):
        self.numberProductions()

        self.columnHeader = []
        self.columnHeader.extend(self.grammar.getTerminals())
        self.columnHeader.append("$")

        self.parseTable.put(("$", "$"), (["acc"], -1))
        for terminal in self.grammar.getTerminals():
            self.parseTable.put((terminal, terminal), (["pop"], -1))

        for key, value in self.numberedProductions.items():
            startSymbol = key[0]
            rules = key[1]
            pos = value

            tableValue = (rules, pos)
            for symbol in self.columnHeader:

                tableKey = (startSymbol, symbol)

                if rules[0] == symbol and symbol != "epsilon":
                    if not self.parseTable.containsKey(tableKey):
                        self.parseTable.put(tableKey, tableValue)

                elif rules[0] in self.grammar.getNonTerminals() and symbol in self.firstSet[rules[0]]:
                    if not self.parseTable.containsKey(tableKey):
                        self.parseTable.put(tableKey, tableValue)
                else:
                    if rules[0] == "epsilon":
                        for b in self.followSet[startSymbol]:
                            if not self.parseTable.containsKey((startSymbol, b)):
                                self.parseTable.put((startSymbol, b), tableValue)
                    else:
                        firsts = []
                        for rule in rules:
                            if rule in self.grammar.getNonTerminals():
                                firsts.extend(self.firstSet[rule])
                        firsts = set(firsts)
                        if "epsilon" in firsts:
                            for b in self.firstSet[startSymbol]:
                                if b == "epsilon":
                                    b = "$"
                                tableKey = (startSymbol, b)
                                if not self.parseTable.containsKey(tableKey):
                                    self.parseTable.put(tableKey, tableValue)

    def parse(self, w):
        self.alpha.clear()
        self.alpha.append("$")
        for char in reversed(w):
            self.alpha.append(char)

        self.beta.clear()
        self.beta.append("$")
        self.beta.append(self.grammar.getStartingSymbol())

        self.pi.clear()
        self.pi.append("epsilon")

        go = True
        status = True
        errorIndex = 0

        while go:
            alphaTop = self.alpha[-1]
            betaTop = self.beta[-1]
            print(self.alpha)
            print(self.beta)

            if alphaTop == "$" and betaTop == "$":
                return status, errorIndex

            parseTableValue = self.parseTable.getKeyValue((betaTop, str(alphaTop)))
            print(parseTableValue)

            if parseTableValue is None:
                go = False
                status = False
            else:
                rules = parseTableValue[0]
                index = parseTableValue[1]

                if index == -1 and rules[0] == "acc":
                    go = False
                    status = True
                elif index == -1 and rules[0] == "pop":
                    self.alpha.pop()
                    self.beta.pop()
                    errorIndex += 1
                else:
                    self.beta.pop()
                    if not rules[0] == "epsilon":
                        for char in reversed(rules):
                            self.beta.append(char)
                    self.pi.append(str(index))

        return status, errorIndex
