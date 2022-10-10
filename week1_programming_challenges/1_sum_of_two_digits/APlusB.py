def sum_of_two_digits(first_digit, second_digit):
    """
    Input: 2 integer numbers
    Output: sum of these 2 numbers
    """
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
