def fibonacci_sum(n):
    # if n <= 1:
    #     return n

    # previous, current, _sum = 0, 1, 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     _sum += current

    # return _sum % 10
    
    # Property 1: S_n = F_(n+2) - 1
    # Property 2: The last digits of the Fibonacci sequence repeat in a cycle of 60
    last_digits = [0] * 60
    last_digits[0] = 0
    last_digits[1] = 1
    for i in range(2, len(last_digits)):
        last_digits[i] = (last_digits[i - 1] + last_digits[i - 2]) % 10
    
    if last_digits[(n + 2) % 60] == 0:
        return 9
    else:
        return last_digits[(n + 2) % 60] - 1


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
