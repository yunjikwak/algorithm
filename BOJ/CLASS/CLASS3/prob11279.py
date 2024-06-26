import heapq
import sys
input = sys.stdin.readline

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    
    if x == 0: # extract
        if len(h) == 0:
            print(0)
        else:
            print(-1*heapq.heappop(h))
    else: # add
        heapq.heappush(h, -1*x)