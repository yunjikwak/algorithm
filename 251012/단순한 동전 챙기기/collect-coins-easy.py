N = int(input())

board = []
coin = [[] for _ in range(11)]
for i in range(N):
    board.append(list(input().strip()))
    for j in range(len(board[i])):
        if board[i][j] == 'S':
            coin[0] = (i, j)
        elif board[i][j] == 'E':
            coin[10] = (i, j)
        elif board[i][j] == '.':
            continue
        else:
            coin[int(board[i][j])] = (i, j)

# dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
arr = [0]

# def in_range(a, b):
#     return 0<=a<N and 0<=b<N

def calc(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def bt(idx, cnt):
    if idx == 10: # 10번까지 탐색
        # 도착 안했거나 cnt가 딸림
        if arr[-1] != 10 or cnt < 5: 
            total = N**N
        else:
            total = 0 # 거리 0
        return total

    tmp = N**N
    for i in range(idx+1, 11):
        if coin[i] == []:
            continue
        tmp = min(tmp, bt(i, cnt))
        arr.append(i)
        tmp = min(tmp, bt(i, cnt+1)+calc(coin[arr[-2]], coin[i]))
        arr.pop()
    return tmp

result = bt(0, 1)
if result == N**N:
    print(-1)
else:
    print(result)