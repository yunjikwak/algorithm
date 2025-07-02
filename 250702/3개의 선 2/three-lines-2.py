import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(3):
    if not arr:
        break
    x_cnt = Counter(a[0] for a in arr)
    y_cnt = Counter(a[1] for a in arr)

    max_x, max_x_cnt = x_cnt.most_common(1)[0]
    max_y, max_y_cnt = y_cnt.most_common(1)[0]

    if max_x_cnt >= max_y_cnt:
        arr = [a for a in arr if a[0] != max_x]
    else:
        arr = [a for a in arr if a[1] != max_y]

if not arr:
    print(1)
else:
    print(0)