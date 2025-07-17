import sys
input = sys.stdin.readline

X = int(input())
least_time = sys.maxsize

for i in range(X):
    total = 0
    time_taken = 0
    speed = 0
    while speed <= i:
        speed += 1
        total += speed
        time_taken += 1
    while speed > 1:
        speed -= 1
        total += speed
        time_taken += 1
    if total > X:
        break
    if total < X:
        time_taken += X-total
    least_time = min(time_taken, least_time)
print(least_time)