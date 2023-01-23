def solve(n):
    ans_hash = [0]*n

    for i in range(2, n+1): #getting answers for every num in range n
        a, b = 1000, 1000

        if i % 2 == 0: a = ans_hash[i // 2 - 1]
        
        if i % 3 == 0: b = ans_hash[i // 3 - 1]

        ans_hash[i-1] = min(a, b, ans_hash[i-2]) + 1

    i = ans_hash[-1]
    answ = [0]*(i + 1)
    

    while i != -1:  #reconstructing answer sequence
        answ[i] = n

        if n % 2 == 0 and ans_hash[n//2 - 1] < i:
            n //= 2

        elif n % 3 == 0 and ans_hash[n//3 - 1] < i:
            n //= 3

        else: 
            n -= 1

        i -= 1

    return answ



def main():
    n = int(input())

    answ = solve(n)

    print(len(answ) - 1)
    print(*answ)


if __name__ == "__main__": main()