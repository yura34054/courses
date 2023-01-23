def main():
    hash_table = [-1 for i in range(9999999)]

    for i in range(int(input())):
        inp = input().split()
        operation, number = inp[0], int(inp[1]) - 1

        if operation == 'add':
            hash_table[number] = inp[2]

        elif operation == 'del':
            hash_table[number] = -1

        elif hash_table[number] == -1:
            print('not found') 
        
        else:
            print(hash_table[number])


if __name__ == '__main__': main()