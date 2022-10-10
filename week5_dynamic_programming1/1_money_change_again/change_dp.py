import sys


def change(money):
    # write your code here
    # denominations: 1, 3, 4
    # print('money', money)
    min_coins = [0] * (money+1)
    for m in range(1, money+1):
        min_coins[m] = sys.maxsize
        for coin in [1, 3, 4]:
            # print('m', m)
            # print('coin', coin)
            if m >= coin:
                # print('a')
                # print('money - coin', money-coin) # wrong, money -> m
                num_coins = min_coins[m - coin] + 1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    # print(min_coins)
    return min_coins[-1]


if __name__ == '__main__':
    m = int(input())
    print(change(m))

