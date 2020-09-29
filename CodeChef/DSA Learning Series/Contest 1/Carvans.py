import sys
T = int(sys.stdin.readline())
while T:
    n = int(sys.stdin.readline())
    speeds = list(map(int, sys.stdin.readline().split()))
    top = 1
    for i in range(1, n):
        if speeds[i] <= speeds[i-1]:
            top += 1
    print(top)
    T -= 1