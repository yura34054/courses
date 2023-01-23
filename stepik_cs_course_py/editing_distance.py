def get_ED(string1: str, string2: str) -> int:

    prev = [i for i in range(len(string1)+1)]

    for i in range(1, len(string2)+1):
        curr = [0 for _ in range(len(string1)+1)]
        curr[0] = i

        for j in range(1, len(string1)+1):

            del_cost = prev[j] + 1
            ins_cost = curr[j-1] + 1
            subst_cost = prev[j-1] + (string1[j-1] != string2[i-1])

            curr[j] = min(del_cost, ins_cost, subst_cost)

        prev = curr

    return prev[-1]


def main():
    print(get_ED(input(), input()))


if __name__ == '__main__': main()