import math

def optimal_summands(n):
    summands = []
    # n = 8 => summands = [1, 2, 5]
    # n = 6 => summands = [1, 2, 3]
    # Explaination: The smallest number that can be made with k different summands 
    # is just the sum of all numbers from 1 to k. Any number smaller than that will have fewer summands... at most k-1
    # To maximize k, we need to find k such that 1+2+...+k = k(k+1) / 2 <= n
    # After k is found, to make the sum of k different summands equal to n, 
    # we calculate 1+2+...+(k-1) = k(k-1) / 2 and then the k-th summand as n - k(k-1) / 2

    k = math.floor((-1 + math.sqrt(1+8*n)) / 2)
    for i in range(1, k):
        summands.append(i)
    summands.append(int(n - k*(k-1) / 2))
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
