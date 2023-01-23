def main():
    cases = [
        [10,14,11],
        [3,20,4,30,21,30,5,31,60,30,21,31],
        [3,20,4,30,21,30,5,31,60,30,31,31]
    ]

    for case in cases:
        for i, weight in enumerate(case, start=1):
            if i // 2 in range(1, len(case) + 1):
                if case[(i // 2) - 1] > weight:
                    break

        else:
            print(f'{case} - True')

            

if __name__ == "__main__": main()