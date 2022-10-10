from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    """
    Input: 2 sequences of integers
    Output: Maximum dot product of 2 sequences

    Find maximum of first_sequence, maximum of second_sequence
    Take away 2 values and then continue until one of the sequence is empty

    # naive solution
    # max_product = 0
    # for permutation in permutations(second_sequence):
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)

    # return max_product
    """

    # second_sequence: clicks, first_sequence: prices   
    max_product = 0
    clicks = second_sequence
    prices = first_sequence

    while clicks and prices:
        c, p = 0, 0
        for i in range(len(clicks)):
            if clicks[i] > clicks[c]:
                c = i

        for i in range(len(prices)):
            if prices[i] > prices[p]:
                p = i
        max_product += clicks[c] * prices[p]

        clicks.pop(c)
        prices.pop(p)

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
