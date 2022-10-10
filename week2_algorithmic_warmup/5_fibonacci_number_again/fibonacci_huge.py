def fibonacci_huge(n, m):
    """
    Input: 2 integers n, m
    Output: The n-th Fibonacci number modulo m

    To compute, say, F2015 mod 3 we just need to find the remainder of 2015
    when divided by 8. Since 2015 = 251*8 + 7, we conclude that 
    F2015 mod 3 = F7 mod 3 = 1

    Read Learning Algorithms Through Programming and Puzzle Solving slides
    Pisano period: https://www.geeksforgeeks.org/fibonacci-number-modulo-m-and-pisano-period/

    # naive solution
    # if n <= 1:
    #     return n

    # previous = 0
    # current  = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current

    # return current % m
    """
    # The period always starts with 01
    # Fi mod m is periodic for every m
    # the period of Fi mod m does not exceed m^2
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
    print(fibonacci_huge(n, m))
