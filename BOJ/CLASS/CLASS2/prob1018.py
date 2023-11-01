N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def diff(x, y):
    cntB = 0
    cntW = 0
    
    for i in range(8):
        for j in range(8):
            if i%2 == 0:
                if j%2 == 0:
                    if board[x+i][y+j] == 'B':
                        cntB += 1
                    else:
                        cntW += 1
                else:
                    if board[x+i][y+j] == 'B':
                        cntW += 1
                    else:
                        cntB += 1
            else:
                if j%2 == 0:
                    if board[x+i][y+j] == 'B':
                        cntW += 1
                    else:
                        cntB += 1
                else:
                    if board[x+i][y+j] == 'B':
                        cntB += 1
                    else:
                        cntW += 1
    return min(cntB, cntW)

min_cnt = 64
for i in range(N - 7):
    for j in range(M - 7):
        tmp = diff(i, j)
        if min_cnt > tmp:
            min_cnt = tmp
print(min_cnt)