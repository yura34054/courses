def solve(n, ladder):
    ans_map = [0, 0]

    for i in range(n):
        ans_map.append(max(ans_map[i+1]+ladder[i], ans_map[i]+ladder[i]))

    return ans_map[-1]


def main():
    n = int(input())
    print(solve(n, list(map(int, input().split()))))


if __name__ == "__main__": main()