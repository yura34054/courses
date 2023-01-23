def bin_search(lst, val):
    l ,r = 0, len(lst) - 1

    while l <= r:
        k = (l + r) // 2

        if lst[k] == val:
            return k + 1

        elif val < lst[k]:
            r = k - 1

        else:
            l = k + 1

    return -1


def main():
    lst = list(map(int, input().split()))[1:]

    for val in list(map(int, input().split()))[1:]:
        print(bin_search(lst, val), end=' ')

if __name__ == '__main__': main()