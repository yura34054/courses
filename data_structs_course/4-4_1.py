def print_in_order(tree, key):
    if key == -1: return

    print_in_order(tree, tree[key][1])
    print(tree[key][0], end=' ')
    print_in_order(tree, tree[key][2])


def print_pre_order(tree, key):
    if key == -1: return

    print(tree[key][0], end=' ')
    print_pre_order(tree, tree[key][1])
    print_pre_order(tree, tree[key][2])


def print_post_order(tree, key):
    if key == -1: return

    print_post_order(tree, tree[key][1])
    print_post_order(tree, tree[key][2])
    print(tree[key][0], end=' ')


def main():
    n = int(input())
    tree = []

    for _ in range(n):
        tree.append(tuple(map(int, input().split())))


    print_in_order(tree, 0)
    print()
    print_pre_order(tree, 0)
    print()
    print_post_order(tree, 0)


if __name__ == '__main__': main()