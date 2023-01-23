def main():
    k, l = map(int , input().split())
    code_table = dict()

    for _ in range(k):
        char, code = input().split(': ')

        code_table[code] = char

    strig = list(input())
    strig.reverse()

    answ, code = '', ''

    while len(strig) != 0:
        code += strig.pop()

        if code in code_table:
            answ += code_table[code]
            code = ''

    print(answ)




if __name__ == '__main__': main()