class Variable:

    def __init__(self) -> None:
        self.parrent = self
        self.rank = 1

    
    @staticmethod
    def get_parrent(variable):
        path = [variable]
        while variable.parrent != variable:
            variable = variable.parrent

        for v in path: v.parrent = variable
        return variable


    @staticmethod
    def merge(variable_1, variable_2):
        if variable_1.rank > variable_2.rank:
            variable_2.parrent = variable_1

        elif variable_1.rank == variable_2.rank:
            variable_2.parrent = variable_1
            variable_1.rank += 1

        else:
            variable_1.parrent = variable_2


def main():
    n, e, d = map(int, input().split())
    variables = [Variable() for i in range(n)]

    for _ in range(e):
        i, j = map(int, input().split())
        Variable.merge(variables[i-1], variables[j-1])

    for _ in range(d):
        i, j = map(int, input().split())
        if Variable.get_parrent(variables[i-1]) == Variable.get_parrent(variables[j-1]):
            print(0)
            return

    print(1)

if __name__ == '__main__': main()

