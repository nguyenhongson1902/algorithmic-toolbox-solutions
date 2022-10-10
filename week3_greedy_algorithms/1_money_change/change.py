def change(money):
    # write your code here
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
