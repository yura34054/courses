def count_sort(lst):
    counter = [0 for _ in range(11)]
    new_lst = []

    for i in lst:
        counter[i] += 1

    for i in range(11):
        for j in range(counter[i]):
            new_lst.append(i)
        
    return new_lst

def main():
    n = input()

    print(*count_sort(list(map(int, input().split()))))

if __name__ == '__main__': main()