def hash_string(s):
    return (sum([ord(s[i])*(x**i) for i in range(len(s))]) % p) % m


def find(table, s):
    if s in table[hash_string(s)]:
        return True

    return False


def main():
    global m
    global p
    global x
    p = 1000000007
    x = 263

    m = int(input())

    table = [[] for i in range(m)]

    for i in range(int(input())):
        operation, value = input().split()

        if operation == 'add':
            if find(table, value) == False:
                table[hash_string(value)].insert(0, value)

        elif operation == 'del':
            if find(table, value) == True:
                table[hash_string(value)].remove(value)

        elif operation == 'find':
            if find(table, value) == True: 
                print('yes')
                                                        
            else: 
                print('no')

        else: # check
            print(' '.join(table[int(value)]))


if __name__ == '__main__': main()