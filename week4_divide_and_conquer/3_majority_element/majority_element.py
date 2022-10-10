# def majority_element_naive(elements):
#     for e in elements:
#         if elements.count(e) > len(elements) / 2:
#             return 1

#     return 0


def count_frequency(elements, left, right, key):
    count = 0
    for i in range(left, right+1):
        if elements[i] == key:
            count += 1
    return count

def majority(elements, left, right):
    if left == right:
        return elements[left]

    mid = (left + right) // 2
    left_majority_element = majority(elements, left, mid)
    right_majority_element = majority(elements, mid+1, right)

    if left_majority_element == right_majority_element:
        return right_majority_element

    count_left = count_frequency(elements, left, right, left_majority_element)
    count_right = count_frequency(elements, left, right, right_majority_element)
    # print('count left', count_left)
    # print('count right', count_right)
    if count_left < count_right:
        return right_majority_element
    else:
        return left_majority_element


def majority_element(elements):
    # O(nlogn) time
    # Property: the majority element of the initial array is also the majority element
    #           of one of the two halves
    # break the initial array into halves and solve each half
    
    result = majority(elements, 0, len(elements) - 1)
    count = 0
    for e in elements:
        if e == result:
            count += 1
    if count > len(elements) // 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
