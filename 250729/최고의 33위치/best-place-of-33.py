import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(0, N-2):
    for j in range(0, N-2):
        cnt = 0
        for p in range(0, 3):
            for q in range(0, 3):
                if map[i+p][j+q] == 1:
                    cnt += 1
        result = max(result, cnt)
print(result)