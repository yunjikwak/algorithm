import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

result = abs(a-b) + abs(c-d)
if a < c and b > c:
    result -= b-c
elif a > c and d > a:
    result -= d-a
print(result)