import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize

N = int(input())
rooms = []

for _ in range(N):
    rooms.append(int(input()))

min_dist = INT_MAX
for i in range(N):
    cur_dist = 0
    for j in range(N): 
        idx = (i+j) % N
        cur_dist += rooms[idx]*abs(j)
    if min_dist > cur_dist:
        min_dist = cur_dist
print(min_dist)