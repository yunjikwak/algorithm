L, N, Q = map(int, input().split())
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
class Knight:
    def __init__(self, r, c, h, w, k):
        self.si = r
        self.sj = c
        self.h = h
        self.w = w
        self.power = k
        self.total_damage = 0

    def is_alive(self):
        return self.power >= 0

    def is_pushed(self, knight, d):
        nx, ny = knight.si+dxs[d], knight.sj+dys[d]
        nex, ney = nx+knight.h-1, ny+knight.w-1

        sx, sy = self.si, self.sj
        ex, ey = sx+self.h-1, sy+self.w-1

        # if (nex < sx or ex < nx) and (ney < sy or ey < ny):
        #     return False
        if nex < sx or ex < nx or ney < sy or ey < ny:
            return False
        return True

    def can_move(self, d):
        move_sx = self.si + dxs[d]
        move_sy = self.sj + dxs[d]
        move_ex = move_sx+self.h-1
        move_ey = move_sy+self.w-1

        # 밖으로 나감
        if not (1 <= move_sx and 1 <= move_ex and move_sy <= L and move_ey <= L):
            return False

        if 0 < (sum_walls[move_ex][move_ey] - sum_walls[move_ex][move_sy-1]
                + sum_walls[move_sx-1][move_sy-1] - sum_walls[move_sx-1][move_sy]):
            return False

        return True

    def move(self, d):
        self.si += dxs[d]
        self.sj += dys[d]

    def get_damage(self):
        ex, ey = self.si+self.h-1, self.sj+self.w-1
        return (sum_traps[ex][ey] - sum_traps[ex][self.sj-1]
                + sum_traps[self.si-1][self.sj-1]
                - sum_traps[self.si-1][ey])

    def desc_power(self, damage):
        damage = max(0, min(self.power, damage))
        self.power -= damage
        self.total_damage += damage


board = [[0] * (L+1) for _ in range(L+1)]
for i in range(1, L+1):
    row = list(map(int, input().split()))
    for j in range(1, L+1):
        board[i][j] = row[j-1]

# 누적합 계산
sum_traps = [[0] * (L+1) for _ in range(L+1)]
for i in range(1, L+1):
    for j in range(1, L+1):
        if board[i][j] == 1:
            a = 1
        else:
            a = 0
        sum_traps[i][j] = sum_traps[i-1][j] + sum_traps[i][j-1] - sum_traps[i-1][j-1] + a

sum_walls = [[0] * (L+1) for _ in range(L+1)]
for i in range(1, L+1):
    for j in range(1, L+1):
        if board[i][j] == 2:
            a = 1
        else:
            a = 0
        sum_walls[i][j] = sum_walls[i-1][j] + sum_walls[i][j-1] - sum_walls[i-1][j-1] + a

knights = []
for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    knights.append(Knight(r,c,h,w,k))

visited = [False] * N
def dfs(idx, d):
    global visited, knights

    visited[idx] = True

    if not knights[idx].can_move(d):
        return False

    # 밀려나는 기사 찾기
    for i in range(N):
        if not visited[i] and knights[i].is_alive() and knights[i].is_pushed(knights[idx], d):
            if not dfs(i, d):
                return False
    return True


def move_knight(idx, d):
    # 체스판 위 존재 확인
    if not knights[idx].is_alive():
        return

    # 연쇄 이동 가능성 판별
    visited = [False] * N
    if not dfs(idx, d):
        return

    # 실제 이동 + 대미지 계산
    for i in range(N):
        if visited[i]:
            knights[i].move(d)
            if i != idx:
                damage = knights[i].get_damage()
                knights[i].desc_power(damage)

for _ in range(Q):
    i, d = map(int, input().split())
    move_knight(i-1, d)

answer = 0
for idx in range(N):
    if knights[idx].is_alive():
        answer += knights[idx].total_damage
print(answer)
