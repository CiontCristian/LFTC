from Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar.read("g3.txt")
        self.firstSet = {}
        self.followSet = {}
        self.populateFirstSet()
        self.populateFollowSet()

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
