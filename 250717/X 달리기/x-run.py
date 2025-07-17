import sys
input = sys.stdin.readline

X = int(input())
min_time = sys.maxsize

for i in range(1, X+1):
    time_taken = (2 * i) - 1
    total = i * i
    
    if total < X:
        remain = X - total
        additional_time = (remain + i - 1) // i
        time_taken += additional_time

    min_time = min(time_taken, min_time)
print(min_time)