from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    # distance:d, tank: m
    location = 0
    if location + tank >= distance:
        return 0
    if (not stops) or (stops[0] - location > tank):
        return -1
    
    last_stop = location
    while stops and stops[0] - location <= tank:
        last_stop = stops[0]
        del stops[0] # warning
        # stops.pop(0) # warning
        # stops = stops[1:] # time limit exceeded

    
    for i in range(len(stops)):
        stops[i] -= last_stop
 
    eval = min_refills(distance - last_stop, tank, stops) # There must be this line because every time we call min_fills(), stops is globally changed. We need the function is called once
    if eval == -1:
        return -1
    else:
        return 1 + eval
    


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
