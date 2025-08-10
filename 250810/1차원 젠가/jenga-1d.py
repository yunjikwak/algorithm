import sys
input = sys.stdin.readline

N = int(input())
block = [int(input()) for _ in range(N)]
remove = list(tuple(map(int, input().split())) for _ in range(2))

result = block
for s, e in remove:
    result = result[:s-1] + result[e:]

print(len(result))
for n in result:
    print(n)