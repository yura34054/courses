def TB_bakpak(W, n, lst):
    ans_hash = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):

            if lst[i-1] <= j:
                ans_hash[i][j] = max(ans_hash[i-1][j], ans_hash[i-1][j-lst[i-1]] + lst[i-1])

            else:
                ans_hash[i][j] = ans_hash[i-1][j]

    return ans_hash[n][W]


def main():
    W, n = map(int, input().split())
    lst = list(map(int, input().split()))

    print(TB_bakpak(W, n, lst))

if __name__ == '__main__': main()