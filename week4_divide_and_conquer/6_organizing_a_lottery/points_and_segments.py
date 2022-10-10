from sys import stdin
from random import randint

def is_less(a, b):
    if a[0] < b[0]:
        return True
    elif a[0] > b[0]:
        return False
    else:
        if a[1] < b[1]:
            return True
        else:
            return False

def is_equal(a, b):
    if a[0] == b[0] and a[1] == b[1]:
        return True
    return False


def partition3(array, left, right):
    # write your code here
    pivot = array[left]

    low = left + 1
    high = right
    mid = left + 1
    while mid <= high:
        # if array[mid] < pivot:
        if is_less(array[mid], pivot):
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        # elif array[mid] == pivot:
        elif is_equal(array[mid], pivot):
            mid += 1
        elif not is_less(array[mid], pivot) and not is_equal(array[mid], pivot):
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    array[left], array[low-1] = array[low - 1], array[left]
    
    return low-1, high

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right) # choose the pivot index
    array[left], array[k] = array[k], array[left] # swap the pivot to left element, which is the pivot position
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

# def points_cover_naive(starts, ends, points):
#     assert len(starts) == len(ends)
#     count = [0] * len(points)

#     for index, point in enumerate(points):
#         for start, end in zip(starts, ends):
#             if start <= point <= end:
#                 count[index] += 1

#     return count

def points_cover(starts, ends, points):
    LEFT, POINT, RIGHT = 1, 2, 3
    new_list = []
    for start in starts:
        new_list.append((start, LEFT))
    for end in ends:
        new_list.append((end, RIGHT))
    for point in points:
        new_list.append((point, POINT))
    
    randomized_quick_sort(new_list, 0, len(new_list) - 1)
    # new_list now is sorted
    points_count = [0] * len(points)

    # a dictionary to keep the indices of points
    points_index = {}
    for i, p in enumerate(points):
        if p not in points_index:
            points_index[p] = [i]
        else:
            points_index[p].append(i)
    
    count = 0
    for element in new_list:
        value, label = element[0], element[1]
        if label == LEFT:
            count += 1
        elif label == POINT:
            for i in points_index[value]:
                points_count[i] = count
        elif label == RIGHT:
            count -= 1
    
    return points_count



if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
