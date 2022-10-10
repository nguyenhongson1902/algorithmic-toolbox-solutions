# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    """
    Input: 2 integers m, n (m = from_, n = to)
    Output: The last digit of F_m + F_(m + 1) + ... + F_n

    Property: S_(m -> n) = S_n - S_(m - 1) = F_(n+2) - F_(m+1)

    # naive solution
    # _sum = 0

    # current = 0
    # _next  = 1

    # for i in range(to + 1):
    #     if i >= from_:
    #         _sum += current

    #     current, _next = _next, current + _next
    # return _sum % 10
    """
    

    last_digits = [0] * 60
    last_digits[0] = 0
    last_digits[1] = 1
    for i in range(2, len(last_digits)):
        last_digits[i] = (last_digits[i - 1] + last_digits[i - 2]) % 10

    return (last_digits[(to + 2) % 60] - last_digits[(from_ + 1) % 60]) % 10



if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
