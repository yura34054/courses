def build_tree(freq:list):
    tree = set()

    if len(freq) == 1:
        tree.add((freq[0], 0))

    while len(freq) != 1:
        freq.sort(key=lambda x: x[1], reverse=True)
        node1 = freq.pop()
        node2 = freq.pop()

        freq.append((node1[0]+node2[0], node1[1]+node2[1]))
        tree.add((node1[0], 1))
        tree.add((node2[0], 0))


    tree = list(tree)
    tree.sort(key=lambda x: len(x[0]), reverse=True)


    return tree

        


def main():
    s = input()

    freq = dict()

    for char in s:
        if char in freq:
            freq[char] += 1

        else:
            freq[char] = 1

    tree = build_tree(list(freq.items()))
    code = dict()

    for char in freq:
        for node in tree:

            if char in node[0]:
                if char in code:
                    code[char] += str(node[1])
                
                else:
                    code[char] = str(node[1])

    answ_str = ''

    for char in s:
        answ_str += code[char]

    print(len(code), len(answ_str))

    for char, c in zip(code.keys(), code.values()):
        print(f'{char}: {c}')

    print(answ_str)



if __name__ == '__main__': main()