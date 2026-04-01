import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

A = min(a1, x1)
B = min(b1, y1)
C = max(a2, x2)
D = max(b2, y2)

X = max((C-A), (D-B))

print(X*X)