

def edit_distance(first_string, second_string):
    A = list(first_string)
    B = list(second_string)

    # D = [[0] * (len(B) + 1)] * (len(A) + 1) # It's gonna generate the wrong answer!!!
    D = [[0]*(len(B) + 1) for _ in range(len(A) + 1)]
    D[0] = [i for i in range(len(D[0]))]
    for i in range(len(D)):
        D[i][0] = i
    # print(D)
    for j in range(len(B)): # column-wise traversal
        for i in range(len(A)):
            # print('i + 1', i+1)
            # print('j', j)
            insertion = D[i + 1][j] + 1
            deletion = D[i][j + 1] + 1
            match = D[i][j]
            mismatch = D[i][j] + 1

            if A[i] == B[j]:
                D[i+1][j+1] = min(insertion, deletion, match)
            
            else:
                D[i+1][j+1] = min(insertion, deletion, mismatch)
    return D[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
