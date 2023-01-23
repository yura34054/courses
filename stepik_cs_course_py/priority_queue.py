class Queie:
    
    def __init__(self) -> None:
        self.__queie = list()

    
    def shift_doun(self, index:int) -> None:
        
        while index*2 <= len(self.__queie):

            offset = -1

            if index*2 + 1 <= len(self.__queie):
                if self.__queie[index*2] > self.__queie[index*2-1]:
                    offset = 0

            if self.__queie[index-1] < self.__queie[index*2+offset]:
                self.__queie[index-1], self.__queie[index*2+offset] = self.__queie[index*2+offset], self.__queie[index-1]
                index = index*2 + offset + 1

            else:
                return None
            

    def shift_up(self, index:int) -> None:

        while index//2 > 0:

            if self.__queie[index-1] > self.__queie[index//2-1]:
                self.__queie[index//2-1], self.__queie[index-1] = self.__queie[index-1], self.__queie[index//2-1]
                index //= 2

            else:
                return None


    def pop(self) -> int:
        if len(self.__queie) == 1:
            max_val = self.__queie.pop()

        else:
            max_val, self.__queie[0] = self.__queie[0], self.__queie.pop()
            self.shift_doun(1)

        return max_val


    def add(self, val:int) -> None:
        self.__queie.append(val)
        self.shift_up(len(self.__queie))



def main():
    queie = Queie()

    for _ in range(int(input())):
        opp = input()

        if opp.startswith('Insert'):
            queie.add(int(opp.split()[1]))

        else:
            print(queie.pop())


if __name__ == '__main__': main()