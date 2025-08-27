import sys
input = sys.stdin.readline

T = int(input())

# U D L R
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inRange(a,b):
    return 0<=a<N and 0<=b<N

def search_marble(arr):
    marble = []
    for i in range(N):
        for j  in range(N):
            if arr[i][j][0] == 1:
                marble.append((i, j, arr[i][j][1]))
    return marble

def opposite(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    elif d == 3: return 2

for _ in range(T):
    N, M = map(int, input().split())
    cnt = [[[0,0] for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        x, y, d = input().split()
        if d == 'U': d = 0
        elif d == 'D': d = 1
        elif d == 'L': d = 2
        elif d == 'R': d = 3
        cnt[int(x)-1][int(y)-1] = [1, d]

    for _ in range(2 * N):
        n_cnt = [[[0,0] for _ in range(N)] for _ in range(N)]
        marble = search_marble(cnt)

        if not marble:
            break

        for x, y, d in marble:
            nx = x+dx[d]
            ny = y+dy[d]

            if inRange(nx, ny):
                n_cnt[nx][ny][0] += 1
                n_cnt[nx][ny][1] = d
            else:
                n_cnt[x][y][0] += 1
                n_cnt[x][y][1] = opposite(d)

        changed = False
        new = [[[0,0] for _ in range(N)] for _ in range(N)]

        for r in range(N):
            for c in range(N):
                if n_cnt[r][c][0] > 1:
                    continue
                elif n_cnt[r][c][0] == 1:
                    new[r][c][0] = 1
                    new[r][c][1] = n_cnt[r][c][1]
                else:
                    new[r][c] = [0,0]

        if new == cnt:
            break
        cnt = new
        
    result = 0
    for i in range(N):
        for j in range(N):
            if cnt[i][j][0] == 1:
                result += 1
    print(result)