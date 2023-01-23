def check_search_rule(tree, key, left_lim, right_lim):
    if key == -1: return
    val, left_child, right_child = tree[key]

    if not left_lim <= val < right_lim:
        raise ValueError('Not a search tree')

    check_search_rule(tree, left_child, left_lim, val)
    check_search_rule(tree, right_child, val, right_lim)


def main():
    n = int(input())
    import sys
    sys.setrecursionlimit(1000 if n < 1000 else n+100)
    
    tree = []

    for _ in range(n):
        tree.append(tuple(map(int, input().split())))

    if n == 0: 
        print('CORRECT')

    else:
        try:
            check_search_rule(tree, 0, -2**32, 2**32)
            print('CORRECT')

        except ValueError:
            print('INCORRECT')


if __name__ == '__main__': main()