def main():
    n = int(input())
    lines = list()
    points = list()

    for _ in range(n):
        lines.append(tuple(map(int, input().split())))

    lines.sort(key=lambda x: x[1])

    for line in lines:
        if len(points) == 0:
            points.append(line[1])
            continue

        if points[-1] not in range(line[0], line[1]+1):
            points.append(line[1])

    print(len(points))
    print(*points)


if __name__ == '__main__': main()