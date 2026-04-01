import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, 1, 1]
dy = [1, -1, -1, 1]

def is_valid(x,y):
    return 0 <= x < N and 0 <= y < N

result = 0
for x in range(N):
    for y in range(N):
        for i in range(1, N):
            for j in range(1, N):
                acc = 0
                cur_x, cur_y = x, y
                valid = True
                
                lens = [i, j, i, j]
                for d in range(4):
                    for _ in range(lens[d]):
                        cur_x += dx[d]
                        cur_y += dy[d]

                        if not is_valid(cur_x, cur_y):
                            valid = False
                            break
                        
                        acc += graph[cur_x][cur_y]
                    
                    if not valid:
                        break
                
                if valid and (cur_x, cur_y) == (x, y):
                    result = max(result, acc)

print(result)