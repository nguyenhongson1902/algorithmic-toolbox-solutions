def gcd(a, b):
    """
    Input: 2 integers a, b
    Output: the greatest common divisor between a and b

    # naive solution
    # current_gcd = 1
    # for d in range(2, min(a, b) + 1):
    #     if a % d == 0 and b % d == 0:
    #         if d > current_gcd:
    #             current_gcd = d
    # return current_gcd

    """

    if a == 0:
        return b
    elif b == 0:
        return a
    
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
