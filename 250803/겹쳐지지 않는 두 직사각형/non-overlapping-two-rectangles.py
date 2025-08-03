import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def cal_val(start_x, start_y, end_x, end_y):
    result = 0
    for i in range(start_x, end_x+1):
        for j in range(start_y, end_y+1):
            result += graph[i][j]
    return result

def max_val(x1,y1,x2,y2):
    max_total = -sys.maxsize
    for i in range(x1, x2):
        for j in range(i, x2):
            for k in range(y1, y2):
                for m in range(k, y2):
                    max_total = max(max_total, cal_val(i,k,j,m))
    return max_total

result = -sys.maxsize
for col in range(1, M):
    a = max_val(0, 0, N, col)
    b = max_val(0, col, N, M)
    result = max(result, a+b)
for row in range(1, N):
    a = max_val(0, 0, row, M)
    b = max_val(row, 0, N, M)
    result = max(result, a+b)
print(result)