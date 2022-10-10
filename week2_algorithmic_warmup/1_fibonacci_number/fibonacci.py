def fibonacci_number(n):
    if n == 0:
        return 0

    fib_numbers = [0] * (n+1)
    fib_numbers[0] = 0
    fib_numbers[1] = 1

    for i in range(2, len(fib_numbers)): # Loop run in O(n) times
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2] # O(n) each time
    
    return fib_numbers[-1]



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

# Time complexity: O(n^2)