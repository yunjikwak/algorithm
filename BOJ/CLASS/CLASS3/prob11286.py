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
            print(heapq.heappop(h)[1])
    else: # tuple로 저장할 시 첫번째 요소로 정렬됨 -> 이후 뒤에 요소로 알아서 정렬됨
        heapq.heappush(h, (abs(x), x))