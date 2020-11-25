from Grammar import *
from Parser import *

if __name__ == '__main__':
    grammar = Grammar.read("g3.txt")
    #print(grammar.getProductionsContainingNonterminal("B"))
    #grammar.run()

    parser = Parser()
    print(parser.firstSet)
    print(parser.followSet)

