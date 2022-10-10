import sys


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def min_max(i, j, m, M, ops):
    minimum = sys.maxsize # infinity
    maximum = -sys.maxsize # -infinity

    for k in range(i, j):
        # print('i=', i)
        # print('k=', k)
        # print('j+1=', j+1)
        a = evaluate(M[i][k], M[k+1][j], ops[k])
        b = evaluate(M[i][k], m[k+1][j], ops[k])
        c = evaluate(m[i][k], M[k+1][j], ops[k])
        d = evaluate(m[i][k], m[k+1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    
    return minimum, maximum



def maximum_value(dataset):
    """
    Reference: https://towardsdatascience.com/course-1-algorithmic-toolbox-part-4-dynamic-programming-223ffc01984a
    """
    ops = [dataset[i] for i in range(len(dataset)) if i % 2 != 0]
    nums = [int(dataset[i]) for i in range(len(dataset)) if i % 2 == 0]
    # print(ops)
    # print(nums)
    m = [[0]*len(nums) for _ in range(len(nums))]
    M = [[0]*len(nums) for _ in range(len(nums))]
    for i in range(len(nums)):
        m[i][i] = nums[i]
        M[i][i] = nums[i]
    # print('m', m)
    # print('M', M)
    for s in range(1, len(nums)):
        for i in range(0, len(nums) - s):
            j = i + s
            m[i][j], M[i][j] = min_max(i, j, m, M, ops)
    # print('m', m)
    # print('M', M)
    return M[0][-1]




if __name__ == "__main__":
    print(maximum_value(input()))
