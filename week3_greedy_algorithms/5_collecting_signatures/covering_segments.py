from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # points = [3, 6]
    while segments:
        m = 0
        for i in range(len(segments)):
            if segments[i].end < segments[m].end:
                m = i
        points.append(segments[m].end)
        
        drops = []
        for i in range(len(segments)):
            if (points[-1] >= segments[i].start) and (points[-1] <= segments[i].end):
                drops.append(i)
        segments = [segments[i] for i in range(len(segments)) if i not in drops]

    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
