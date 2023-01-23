def main():
    size, n = map(int, input().split())
    queue = []
    
    for i in range(n):
        arr, dur = map(int, input().split())

        for pack in queue:
            if arr >= pack[1]: 
                print(pack[0])
                queue.remove(pack)

        if len(queue) < size:
            st = arr
            if len(queue) > 1 and st < queue[-1][1]:
                st = queue[-1][1]

            queue.append((st, st+dur))

        else:
            print(-1)

    for pack in queue:
        print(pack[0])


if __name__ == '__main__': main()