def main():
    n, w = map(int, input().split())
    objs = list()
    cost = 0

    for _ in range(n):
        objs.append(tuple(map(int, input().split())))

    objs.sort(key=lambda x: 0 if x[0] == 0 else x[1] / x[0])

    for obj in objs:
        if w == 0:
            break

        elif w >= obj[1]:
            cost += obj[0]
            w -= obj[1]

        else:
            cost += obj[0] * (w / obj[1])
            w = 0
            break

    print(round(cost, 5))


if __name__ == '__main__': main()