import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    cur = board[i][0]
    cnt = 1
    for j in range(1, N):
        if cur == board[i][j]:
            cnt += 1
        else:
            cur = board[i][j]
            cnt_row = 1
        
        if cnt >= M:
            result += 1
            break

    cur = board[0][i]
    cnt = 1
    for j in range(1, N):
        if cur == board[j][i]:
            cnt += 1
        else:
            cur = board[j][i]
            cnt = 1
        
        if cnt >= M:
            result += 1
            break

if N == 1 and M == 1:
    result += 2

print(result)