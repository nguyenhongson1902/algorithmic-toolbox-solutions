def fibonacci_last_digit(n):
    """
    Input: An integer number
    Output: The last digit of the n-th Fibonacci number

    Property: the sequence of final digits in Fibonacci numbers repeats in cycles of 60

    https://math.stackexchange.com/questions/113536/fibonaccis-final-digits-cycle-every-60-numbers#:~:text=References%3A,the%20last%20four%20in%20%2C%20etc.

    """
    if n <= 1:
        return n
    last_digits = [0] * 60

    # Stage 1: Find the sequence of the last digits in the first 60 elements of the Fibonacci series
    last_digits[0] = 0
    last_digits[1] = 1
    for i in range(2, len(last_digits)):
        last_digits[i] = (last_digits[i-1] + last_digits[i-2]) % 10 # store the last digit

    # Stage 2: Return the last digit of n
    return last_digits[n % 60]

# Time complexity: O(1)
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
