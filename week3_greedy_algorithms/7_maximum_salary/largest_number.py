from itertools import permutations

def is_better(number, max_number):
    number1 = int(str(number) + str(max_number))
    number2 = int(str(max_number) + str(number))
    if number1 >= number2:
        return True
    else:
        return False

def largest_number_naive(numbers):
    # numbers = list(map(str, numbers))

    # largest = 0

    # for permutation in permutations(numbers):
    #     largest = max(largest, int("".join(permutation)))

    # return largest

    numbers = list(map(int, numbers))
    largest = ''
    while numbers:
        max_number_idx = 0
        max_number = 0
        for idx, number in enumerate(numbers):
            if is_better(number, max_number):
                max_number = number
                max_number_idx = idx
        
        largest += str(max_number)

        numbers.pop(max_number_idx)
    
    return int(largest)



if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
