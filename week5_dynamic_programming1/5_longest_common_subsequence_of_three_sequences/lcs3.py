# import numpy as np

def lcs3(first_sequence, second_sequence, third_sequence):
    # Goal: Maximizing the alignment score (muy = 0, sigma = 0) = Finding the maximum matches
    A = list(first_sequence)
    B = list(second_sequence)
    C = list(third_sequence)

    D = [[[0]*(len(C)+1) for _ in range(len(B)+1)] for _ in range(len(A) + 1)]
    # print(np.array(D).shape)
    for i in range(len(A)): # row-wise traversal
        for j in range(len(B)):
            for k in range(len(C)):
                indel1 = D[i+1][j][k]
                indel2 = D[i][j+1][k]
                indel3 = D[i][j][k+1]
                
                indel4 = D[i+1][j+1][k]
                indel5 = D[i][j+1][k+1]
                indel6 = D[i+1][j][k+1]

                mismatch = D[i][j][k]
                match = D[i][j][k] + 1

                if A[i] == B[j] and A[i] == C[k]:
                    D[i+1][j+1][k+1] = max(indel1, indel2, indel3, indel4, indel5, indel6, match)
                else:
                    D[i+1][j+1][k+1] = max(indel1, indel2, indel3, indel4, indel5, indel6, mismatch)

    return D[-1][-1][-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
