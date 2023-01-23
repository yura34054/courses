"""наибольшая последовательнократная подпоследовательность"""

def solve(lst):
    
    answs = [1 for i in range(len(lst))]

    for i, val in enumerate(lst):
        for j in range(i):

            if val % lst[j] == 0 and answs[j] > answs[i] - 1:
                answs[i] = answs[j] + 1

    return max(answs)



def main():
    n, lst = int(input()), list(map(int, input().split()))

    print(solve(lst))


if __name__ == '__main__': main()

