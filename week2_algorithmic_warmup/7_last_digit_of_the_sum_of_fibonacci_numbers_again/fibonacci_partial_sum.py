# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    # _sum = 0

    # current = 0
    # _next  = 1

    # for i in range(to + 1):
    #     if i >= from_:
    #         _sum += current

    #     current, _next = _next, current + _next
    # return _sum % 10

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
