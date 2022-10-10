def fibonacci_huge_naive(n, m):
    # if n <= 1:
    #     return n

    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % m

    previous, current = 0, 1
    for i in range(m*m):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            pisano_period =  i + 1
            break
    
    n = n % pisano_period
    if n == 0:
        return 0
        
    previous_mod, current_mod = 0, 1
    for _ in range(n - 1):
        previous_mod, current_mod = current_mod, (previous_mod + current_mod) % m
    
    return current_mod



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
