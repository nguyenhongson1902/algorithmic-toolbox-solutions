from random import randint

# O(nlogn) time
def partition3(array, left, right):
    # write your code here
    pivot = array[left]

    low = left + 1
    high = right
    mid = left + 1
    while mid <= high:
        if array[mid] < pivot:
            array[mid], array[low] = array[low], array[mid]
            mid += 1
            low += 1
        elif array[mid] == pivot:
            mid += 1
        else:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    array[left], array[low-1] = array[low - 1], array[left]
    
    return low-1, high




def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
