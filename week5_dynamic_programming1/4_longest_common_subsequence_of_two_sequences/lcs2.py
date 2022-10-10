def lcs2(first_sequence, second_sequence):
    # Goal: Maximizing the alignment score (muy = 0, sigma = 0) = Finding the maximum matches
    A = list(first_sequence)
    B = list(second_sequence)

    D = [[0]*(len(B)+1) for _ in range(len(A) + 1)]

    for i in range(len(A)): # row-wise traversal
        for j in range(len(B)):
            insertion = D[i+1][j]
            deletion = D[i][j+1]
            mismatch = D[i][j]
            match = D[i][j] + 1

            if A[i] == B[j]:
                D[i+1][j+1] = max(insertion, deletion, match)
            else:
                D[i+1][j+1] = max(insertion, deletion, mismatch)

    return D[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
