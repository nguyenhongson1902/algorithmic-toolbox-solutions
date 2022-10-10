def binary_search(keys, query):
    # write your code here
    min_idx = 0
    max_idx = len(keys) - 1
    while min_idx <= max_idx:
        mid_idx = (min_idx + max_idx) // 2
        if keys[mid_idx] == query:
            if mid_idx - 1 < 0:
                return mid_idx
            if keys[mid_idx - 1] != query:
                return mid_idx
            max_idx = mid_idx - 1
        elif keys[mid_idx] > query:
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1
    
    return -1
    


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
