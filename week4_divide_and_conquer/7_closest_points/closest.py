from collections import namedtuple
from itertools import combinations
from math import sqrt
# import sys


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


# def minimum_distance_squared_naive(points):
#     min_distance_squared = float("inf")

#     for p, q in combinations(points, 2):
#         min_distance_squared = min(min_distance_squared,
#                                    distance_squared(p, q))

#     return min_distance_squared

def closest_pair(X, Y): # X, Y are already sorted
    # X is sorted points based on x coordinates
    # Y is sorted points based on y coordinates
    # base cases
    # print()
    # print('X', X)
    # print('Y', Y)
    if len(X) == 2:
        return distance_squared(X[0], X[1])
    if len(X) == 3:
        return min(distance_squared(X[0], X[1]), distance_squared(X[0], X[2]), distance_squared(X[1], X[2]))

    
    mid = len(X) // 2 if len(X) % 2 == 0 else (len(X) // 2) + 1
    # print('X[mid]', X[mid])
    d1 = closest_pair(X[:mid], Y[:mid])
    # print('d1', d1)
    d2 = closest_pair(X[mid:], Y[mid:])
    # print('d2', d2)
    d = min(d1, d2)
    # print('d', d)
    # print('X[mid].x - d', X[mid].x - d)
    # print('X[mid].x + d', X[mid].x + d)
    S = [point for point in Y if ((point.x <= X[mid].x + d) and (point.x >= X[mid].x - d))]
    # print('S', S)
    for i in range(len(S)):
        for j in range(1, 8):
            if i + j < len(S):
                d = min(d, distance_squared(S[i], S[i+j]))

    return d

def minimum_distance_squared(points):
    """
    References:
    https://www.youtube.com/watch?v=6u_hWxbOc7E&ab_channel=LingQi
    https://towardsdatascience.com/course-1-algorithmic-toolbox-part-3-divide-and-conquer-dd9022bfa2c0
    [CLRS] textbook, [section 33.4] about this problem
    [CLRS] Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein. Introduction to Algorithms (3rd Edition). MIT Press and McGraw-Hill. 2009.

    """
    X = sorted(points, key=lambda point: point.x)
    Y = sorted(points, key=lambda point: point.y)
    return closest_pair(X, Y)





if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
