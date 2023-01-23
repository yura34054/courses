from math import floor

def child_1(l, i):
    return -1 if (i+1)*2-1 >= len(l) else l[(i+1)*2-1]


def child_2(l, i):
    return -1 if (i+1)*2 >= len(l) else l[(i+1)*2]


def shift_doun(l, i):
    l_child = 10**10 if (i+1)*2-1 >= len(l) else l[(i+1)*2-1]
    r_child = 10**10 if (i+1)*2 >= len(l) else l[(i+1)*2]

    while l[i] > min(l_child, r_child):

        if l_child < r_child:
            l[i], l[(i+1)*2-1] = l[(i+1)*2-1], l[i]
            answ.append((i, (i+1)*2-1))
            i = (i+1)*2-1

        elif r_child != 10**10:
            l[i], l[(i+1)*2] = l[(i+1)*2], l[i]
            answ.append((i, (i+1)*2))
            i = (i+1)*2

        l_child = 10**10 if (i+1)*2-1 >= len(l) else l[(i+1)*2-1]
        r_child = 10**10 if (i+1)*2 >= len(l) else l[(i+1)*2]


def main():
    n = int(input())
    l = list(map(int, input().split()))
    global answ
    answ = []

    for i in range(floor(n/2), 0, -1):
        shift_doun(l, i-1)

    print(len(answ))
    for swap in answ: print(*swap)

if __name__ == '__main__': main()
