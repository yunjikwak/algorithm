import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def is_valid(x1,y1,x2,y2):
    result = True
    if x1 < 0 or x2 > N or y1 < 0 or y2 > M:
        result = False
    return result

def is_include_negative(r1,c1,r2,c2):
    for r in range(r1, r2):
        for c in range(c1, c2):
            if graph[r][c] <= 0: # 양수!!! 0 이상
                return True
    return False

size = -1
for x in range(N, 0, -1):
    for y in range(M, 0, -1):
        for r in range(N):
            if not is_valid(r, 0, r+x, M-1):
                break

            for c in range(M):
                if not is_valid(r, c, r+x, c+y):
                    continue
                if not is_include_negative(r, c, r+x, c+y):
                    size = max(size, x*y)
print(size)