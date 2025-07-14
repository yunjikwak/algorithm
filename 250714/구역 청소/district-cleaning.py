import sys
input = sys.stdin.readline

a,b = map(int, input().split())
c,d = map(int, input().split())

result = abs(a-b) + abs(c-d)

start = max(a,c)
end = min(b, d)

result -= end-start

print(result)