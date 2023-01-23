"""наибольшая невозрастающая подпоследовательность (за n*log(n))"""

from random import randint
from time import perf_counter


def solve(lst, lst_length):
    pass



def main():
    n, lst = int(input()), list(map(int, input().split()))

    answ = solve(lst, n)

    print(answ[0])
    print(*answ[1])



def test():
    #X1 = [randint(0, 10**9) for _ in range(10**5)]
    #X2 = [10**9 for _ in range(10**5)]
    X3 = [1 for _ in range(10**5)]

    print('first')

    st = perf_counter()

    solve(X3, 10**5)

    fi = perf_counter()

    print(fi - st)


if __name__ =='__main__': main()