def lcm(a, b):
    """
    Input: 2 integers a, b
    Output: the least common multiple of a and b

    Property: lcm(a, b) * gcd(a, b) = a * b

    # naive solution
    # for l in range(1, a * b + 1):
    #     if l % a == 0 and l % b == 0: # (if l is divisible by a and l is divisible by b)
    #         return l
    # assert False
    """
    # Step 1: Compute gcd(a, b)
    def gcd(a, b):
        if a == 0:
            return b
        elif b == 0:
            return a

        if a >= b:
            return gcd(a % b, b)
        else:
            return gcd(a, b % a)

    # Step 2: Compute lcm(a, b)

    return int((a * b) / gcd(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

