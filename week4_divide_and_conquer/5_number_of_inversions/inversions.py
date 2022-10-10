from itertools import combinations



# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions
count = 0

def merge(left_half, right_half):
    """
    See the illustration of merge sort method here
    https://www.geeksforgeeks.org/counting-inversions/
    """
    global count
    sorted_list = []
    # count = 0
    # print('left_half', left_half)
    # print('right_half', right_half)
    while left_half and right_half:
        if left_half[0] <= right_half[0]:
            sorted_list.append(left_half[0])
            left_half.pop(0)
        else:
            sorted_list.append(right_half[0])
            count += len(left_half)
            right_half.pop(0)
    if left_half:
        sorted_list.extend(left_half)
    if right_half:
        sorted_list.extend(right_half)
    # print('count', count)
    return sorted_list

def merge_sort(a, left, right):
    if left == right:
        return [a[left]]
    mid = (left + right) // 2
    left_half = merge_sort(a, left, mid)
    right_half = merge_sort(a, mid + 1, right)
    sorted_list = merge(left_half, right_half)
    return sorted_list
    


def inversions(a):
    sorted_list = merge_sort(a, 0, len(a)-1)
    return count

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions(elements))
