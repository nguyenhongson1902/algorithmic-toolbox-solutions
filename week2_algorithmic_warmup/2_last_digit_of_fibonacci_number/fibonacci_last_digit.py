def fibonacci_last_digit(n):
    if n <= 1:
        return n
    last_digits = [0] * 60
    # Property: the sequence of final digits in Fibonacci numbers repeats in cycles of 60
    # Stage 1: Find the sequence of the last digits in the first 60 elements of the Fibonacci series
    last_digits[0] = 0
    last_digits[1] = 1
    for i in range(2, len(last_digits)):
        last_digits[i] = (last_digits[i-1] + last_digits[i-2]) % 10
    

    # for _ in range(n - 1):
    #     previous, current = current, previous + current


    # Stage 2: Return the last digit of n
    return last_digits[n % 60]

# Time complexity: O(1)
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
