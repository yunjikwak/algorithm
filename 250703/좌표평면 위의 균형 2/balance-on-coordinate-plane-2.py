import sys
input = sys.stdin.readline

N = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

all_x = [p[0] for p in points]
all_y = [p[1] for p in points]

x_start = min(all_x)
x_end = max(all_x)
y_start = min(all_y)
y_end = max(all_y)

result = sys.maxsize
for i in range(x_start+1, x_end):
    if i % 2 != 0:
        continue
    for j in range(y_start+1, y_end):
        if j % 2 != 0:
            continue
        a, b, c, d = 0, 0, 0, 0
        for p in points:
            if p[0] > i and p[1] > j:
                a += 1
            elif p[0] < i and p[1] > j:
                b += 1
            elif p[0] < i and p[1] < j:
                c += 1
            elif p[0] > i and p[1] > j:
                d += 1
    result = min(result, max(a,b,c,d))
print(result)