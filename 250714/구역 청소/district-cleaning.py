import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

result = 0
if a < c and b > d:
    result = abs(a-b)
elif c < a and d > b:
    result = abs(c-d)
else:
    result = abs(a-b) + abs(c-d)
    if a < c and b > c:
        result -= b-c
    elif a > c and d > a:
        result -= d-a
print(result)