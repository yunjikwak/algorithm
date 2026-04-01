import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

### 모든 경우의 수 생각
## 1 > 2, 2 > 3, 3 > 1
## 1 > 3, 3 > 2, 2 > 1
first = [(1,2), (2,3), (3,1)]
second = [(1,3), (3,2), (2,1)]

cnt_first = 0
cnt_second = 0
for a in arr:
    if a in first:
        cnt_first += 1
    elif a in second:
        cnt_second += 1
print(max(cnt_first, cnt_second))