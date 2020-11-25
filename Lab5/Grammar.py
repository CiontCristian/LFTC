class Grammar:
    def __init__(self, N, E, S, P):
        self.N = N
        self.E = E
        self.S = S
        self.P = P

    def getTerminals(self):
        return self.E

    def getNonTerminals(self):
        return self.N

    def getStartingSymbol(self):
        return self.S

    @staticmethod
    def parseLine(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def read(file_name):
        with open(file_name) as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = Grammar.parseLine(file.readline())[0]

            file.readline()

            P = []
            for line in file:
                [lhs, rhs] = line.strip().split('->')
                lhs.strip()
                for token in rhs.strip().split('|'):
                    token = list(filter(lambda a: a != '', token.split(' ')))
                    P.append((lhs.strip(), token))

            return Grammar(N, E, S, P)

    def getProductionsForNonterminal(self, symbol):
        prods = []

        for production in self.P:
            if production[0] == symbol:
                prods.append(production[1])

        return prods

    def getProductionsContainingNonterminal(self, symbol):
        prods = []

        for production in self.P:
            if symbol in production[1]:
                prods.append(production)

        return prods

    def printMenu(self):
        print("0.Exit")
        print("1.Display the set of non-terminals")
        print("2.Display the set of terminals")
        print("3.Display the starting symbol")
        print("4.Display all the productions")
        print("5.Display the productions of a given non-terminal")
        print("6.Show everything")

    def run(self):
        while True:
            try:
                self.printMenu()
                option = int(input("<<:"))
                if option == 0:
                    exit(0)
                elif option == 1:
                    print("N = { " + ', '.join(self.N) + " }\n")
                elif option == 2:
                    print("E = { " + ', '.join(self.E) + " }\n")
                elif option == 3:
                    print("S = { " + str(self.S) + " }")
                elif option == 4:
                    prods = "P = { " + ', '.join([' -> '.join(prod) for prod in self.P]) + " }\n"
                    print(prods)
                elif option == 5:
                    symbol = str(input("Enter symbol: (eg. A)"))
                    print(self.getProductionsForNonterminal(symbol))
                elif option == 6:
                    print(self)
                else:
                    raise Exception("Invalid option!")
            except Exception as e:
                print(e)

    def __str__(self):
        return 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'P = { ' + ', '.join([' -> '.join(prod) for prod in self.P]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'

