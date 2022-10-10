from sys import stdin

def subset_sums(S, n, sum_S1, sum_S2, sum_S3):
    if sum_S1 == 0 and sum_S2 == 0 and sum_S3 == 0:
        return 1
    
    if n < 0:
        return 0
    
    A = 0
    if sum_S1 >= S[n]:
        A = subset_sums(S, n-1, sum_S1 - S[n], sum_S2, sum_S3)
    
    B = 0
    if A != 1 and sum_S2 >= S[n]:
        B = subset_sums(S, n-1, sum_S1, sum_S2 - S[n], sum_S3)

    C = 0
    if A != 1 and B != 1 and sum_S3 >= S[n]:
        C = subset_sums(S, n-1, sum_S1, sum_S2, sum_S3 - S[n])
    
    return A or B or C


def partition3(values):
    if len(values) < 3:
        return 0
    
    total = sum(values)
    if total % 3 != 0:
        return 0
    
    return subset_sums(values, len(values) - 1, total // 3, total // 3, total // 3)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
