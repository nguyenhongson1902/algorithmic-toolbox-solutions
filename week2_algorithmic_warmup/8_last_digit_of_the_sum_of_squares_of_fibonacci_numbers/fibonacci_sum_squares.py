def fibonacci_sum_squares(n):
    # if n <= 1:
    #     return n

    # previous, current, sum = 0, 1, 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     sum += current * current

    # return sum % 10

    last_digits = [0] * 60
    last_digits[0] = 0
    last_digits[1] = 1
    for i in range(2, len(last_digits)):
        last_digits[i] = (last_digits[i - 1] + last_digits[i - 2]) % 10

    return (last_digits[n % 60] * last_digits[(n+1) % 60]) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
