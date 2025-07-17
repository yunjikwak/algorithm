import sys
input = sys.stdin.readline

X = int(input())
min_time = sys.maxsize

for i in range(1, X+1):
    total = 0
    time_taken = 0

    speed = 1

    for up in range(1, i):
        total += up
        time_taken += 1
    total += i
    time_taken += 1
    for down in range(i-1, 0, -1):
        total += down
        time_taken += 1
    if total < X:
        time_taken += X-total
    min_time = min(time_taken, min_time)
print(min_time)