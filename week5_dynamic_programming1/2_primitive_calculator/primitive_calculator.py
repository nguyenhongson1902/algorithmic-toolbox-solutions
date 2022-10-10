
def compute_operations(n):
    if n == 1:
        return [1]
    cache = [1, 0, 1, 1] + [0]*(n-3) # initialized #operations of each i value
    for i in range(4, len(cache)):
        if i % 2 == 0 and i % 3 != 0:
            cache[i] = min(cache[i // 2] + 1, cache[i-1] + 1)
        
        if i % 2 != 0 and i % 3 == 0:
            cache[i] = min(cache[i // 3] + 1, cache[i-1] + 1)
        
        if i % 2 == 0 and i % 3 == 0:
            cache[i] = min(cache[i//2] + 1, cache[i // 3] + 1, cache[i-1] + 1)
        
        if i % 2 != 0 and i % 3 != 0:
            cache[i] = cache[i-1] + 1
    # cache[-1] is #operations needed for value n
    # backtrack the cache in the following
    result = [1] * (cache[-1] + 1)
    for i in range(cache[-1]):
        result[-i-1] = n
        if n % 2 == 0 and n % 3 != 0:
            if cache[n] == cache[n//2] + 1:
                n = n // 2
            else:
                n = n - 1
            continue
        
        if n % 3 == 0 and n % 2 != 0:
            if cache[n] == cache[n//3] + 1:
                n = n // 3
            else:
                n = n - 1
            continue
        
        if n % 2 != 0 and n % 3 != 0:
            n = n - 1
            continue

        if n % 2 == 0 and n % 3 == 0:
            if cache[n] == cache[n//2] + 1:
                n = n // 2
            elif cache[n] == cache[n//3] + 1:
                n = n // 3
            elif cache[n] == cache[n-1] + 1:
                n = n - 1
            continue

    return result





if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    # print(output_sequence)
    print(len(output_sequence) - 1)
    print(*output_sequence)
