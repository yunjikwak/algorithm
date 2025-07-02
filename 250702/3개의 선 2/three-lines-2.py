import sys
from collections import Counter
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

x_arr = [x[0] for x in arr]
x_cnt = Counter(x_arr)

result = 0

for cnt in x_cnt.values():
    if cnt > 1:
        result += 1

y_arr = [y[1] for y in arr]
y_cnt = Counter(y_arr)

for cnt in y_cnt.values():
    if cnt > 1:
        result += 1

if result > 3:
    print(0)
else:
    print(1)