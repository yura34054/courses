from random import randint, shuffle
from bisect import bisect_left, bisect_right


def bin_search(lst, val):
    l, r = 0, len(lst) - 1

    while l <= r:
        k = (l + r) // 2

        if lst[k] == val:
            return k

        elif val < lst[k]:
            r = k - 1

        else:
            l = k + 1

    return k


def count_less(lst, val):
#    pos = bin_search(lst, val)
#
#    while pos >= 0 and lst[pos] >= val:
#        pos -= 1
#
#    return pos + 1

    return bisect_left(lst, val)


def count_less_eq(lst, val):
#    pos = bin_search(lst, val)
#
#    while pos < len(lst) and lst[pos] <= val:
#        pos += 1
#
#    return pos

    return bisect_right(lst, val)


def partition(lst, l, r):
    l1, l2, l3 = [], [], []
    piv = lst[randint(l, r-1)]

    for i in lst[l:r+1]:
        if i < piv:
            l1.append(i)

        elif i == piv:
            l2.append(i)

        else:
            l3.append(i)

    lst[l:r+1] = l1 + l2 + l3

    return l + len(l1), l + len(l1) + len(l2)


def quick_sort(lst, l, r):
    
    if l >= r:
        return 

    m_start, m_end = partition(lst, l, r)
    quick_sort(lst, l, m_start)
    quick_sort(lst, m_end, r)


def main():
    n, m = map(int, input().split())
    starts, ends = [], []

    for i in range(n):
        s, e = map(int, input().split())
        starts.append(s)
        ends.append(e)

    quick_sort(starts, 0, len(starts)-1)
    quick_sort(ends, 0, len(ends)-1)
    
    for i in map(int, input().split()):

        N = count_less_eq(starts, i)
        M = count_less(ends, i)

        print(N - M, end=' ')


if __name__ == '__main__': main()


"""
7 6
6 6
2 3
2 5
3 5
2 7
5 7
3 7
1 2 3 5 6 7
Ответ:

0 3 5 5 4 3 
"""