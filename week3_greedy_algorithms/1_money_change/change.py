def change(money):
    """
    Input: An integer money
    Output: The minimum number of coins with denominations 1, 5, and 10 that changes money.
    
    We try to change as many largest coins with maximal denomination (10) as possible
    and apply the same procedure to 5 and 1

    """
    count = 0
    while money > 0:
        if money >= 10:
            money -= 10
        elif money < 10 and money >= 5:
            money -= 5
        elif money < 5:
            money -= 1
        
        count += 1
    
    return count


if __name__ == '__main__':
    m = int(input())
    print(change(m))
