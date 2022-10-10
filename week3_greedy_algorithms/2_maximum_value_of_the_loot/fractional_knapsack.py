from sys import stdin


def optimal_value(capacity, weights, values):
    # value = 0.
    # write your code here
    if capacity == 0 or not weights:
        return 0.

    prices = []
    for v, w in zip(values, weights):
        prices.append(v / w)

    m = 0 # the index of the most expensive item
    for i in range(len(prices)):
        if prices[i] > prices[m]:
            m = i
    amount = min(weights[m], capacity)
    value = prices[m] * amount

    capacity -= amount
    del weights[m]
    del values[m]


    return value + optimal_value(capacity, weights, values)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
