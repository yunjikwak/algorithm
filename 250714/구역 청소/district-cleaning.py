import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

if b < c or d < a:
    result = abs(a-b) + abs(c-d)
else:
    result = max(b, d) - min(a, c)
print(result)