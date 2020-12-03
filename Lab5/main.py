from Grammar import *
from Parser import *

if __name__ == '__main__':
    grammar = Grammar.read("g3.txt")
    # print(grammar.getProductionsContainingNonterminal("B"))
    # grammar.run()

    parser = Parser()
    print("First: " + str(parser.firstSet))
    print("Follow: " + str(parser.followSet))
    parser.populateParseTable()
    print("Numbered productions: ", str(parser.numberedProductions))
    print("Parse table: " + str(parser.parseTable))

    #parser.parseResult(["(", "a", "+", "a", ")"])
    parser.parseResult(["(","a",")"])
