from collections import Counter


class FiniteAutomata:
    def __init__(self, Q, E, q0, F, T):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.T = T

    @staticmethod
    def parseLine(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def read(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.parseLine(file.readline())
            E = FiniteAutomata.parseLine(file.readline())
            q0 = FiniteAutomata.parseLine(file.readline())[0]
            F = FiniteAutomata.parseLine(file.readline())

            file.readline()

            T = []
            for line in file:
                [lhs, destNode] = line.strip().split('->')
                [startNode, value] = lhs.strip()[1:-1].split(',')
                T.append(((startNode, value.strip()), destNode.strip()))

            return FiniteAutomata(Q, E, q0, F, T)

    def printMenu(self):
        print("0.Exit")
        print("1.Display the set of states")
        print("2.Display the alphabet")
        print("3.Display all the transitions")
        print("4.Display the final states")
        print("5.Display the initial state")
        print("6.Show everything")

    def run(self):
        while True:
            try:
                self.printMenu()
                option = int(input("<<:"))
                if option == 0:
                    exit(0)
                elif option == 1:
                    print("Q = { " + ', '.join(self.Q) + " }\n")
                elif option == 2:
                    print("E = { " + ', '.join(self.E) + " }\n")
                elif option == 3:
                    print("T = { " + str(self.T) + " }")
                elif option == 4:
                    print("F = { " + ', '.join(self.F) + " }\n")
                elif option == 5:
                    print("q0 = { " + self.q0 + " }\n")
                elif option == 6:
                    print(self)
                else:
                    raise Exception("Invalid option!")
            except Exception as e:
                print(e)

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
                                              "E = { " + ', '.join(self.E) + " }\n" \
                                                                             "q0 = { " + self.q0 + " }\n" \
                                                                                                   "F = { " + ', '.join(
            self.F) + " }\n" \
                      "T = { " + str(self.T) + " }"
