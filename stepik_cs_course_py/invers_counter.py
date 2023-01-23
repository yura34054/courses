def merge(lst1, lst2):
    new_lst = []

    global err

    while lst1 and lst2:
        elem1, elem2 = lst1[0], lst2[0]

        if elem1 < elem2:
            new_lst.append(elem1)
            del lst1[0]

        else:
            new_lst.append(elem2)
            del lst2[0]
            err += len(lst1)


    new_lst.extend(lst1 + lst2)

    return new_lst

def mergesort(lst):

    m = len(lst) // 2
    if len(lst) > 1:
        lst = merge(mergesort(lst[:m]), mergesort(lst[m:]))

    return lst

def main():
    global err
    err = 0

    n = input()

    mergesort(list(map(int, input().split())))
    print(err)

if __name__ == '__main__': main()