def fib(n):
    double_prev_n = 0
    prev_n = 1
    
    for i in range(n - 2):
        double_prev_n, prev_n = prev_n, (prev_n + double_prev_n) % 10
        
    return (prev_n + double_prev_n) % 10
        
def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()