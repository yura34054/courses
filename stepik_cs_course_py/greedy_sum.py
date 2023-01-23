def main():
    n = int(input())
    nums = list()

    for i in range(1, n+1):
        if n == 0:
            break

        elif i <= n and n-i > i or n-i == 0:
            n -= i
            nums.append(i)

    print(len(nums))
    print(*nums)

if __name__ == '__main__': main()