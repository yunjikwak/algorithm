import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def inRange(a,b):
    return 0<=a<N and 0<=b<N

def opposite(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    elif d == 3: return 2

def cal_time(m1, m2):
    x1, y1, w1, d1, i1 = m1
    x2, y2, w2, d2, i2 = m2

    vx1, vy1 = dx[d1], dy[d1]
    vx2, vy2 = dx[d2], dy[d2]

    if vx1 == vx2 and vy1 == vy2: # 평행 이동
        return None  

    tx = None
    ty = None

    if vx1 != vx2:
        tx = (x2 - x1) / (vx1 - vx2)
    if vy1 != vy2:
        ty = (y2 - y1) / (vy1 - vy2)

    if tx is not None and ty is not None:
        if tx == ty and tx > 0:
            return tx
    elif tx is not None and vy1 == vy2 and tx > 0:
        return tx
    elif ty is not None and vx1 == vx2 and ty > 0:
        return ty
    return None

T = int(input())
for _ in range(T):
    N = int(input())

    marble = []
    for i in range(N):
        x, y, w, d = input().split()

        if d == 'U': d = 0
        elif d == 'D': d = 1
        elif d == 'L': d = 2
        elif d == 'R': d = 3

        marble.append([(int(x)-1)*2, (int(y)-1)*2, int(w), d, i])
    
    cnt = []
    for i in range(N):
        for j in range(i+1, N):
            t = cal_time(marble[i], marble[j])

            if t is not None and t > 0:
                cnt.append((t, i, j))
    
    cnt.sort()

    is_valid = [True] * N
    last_t = -1

    for t, i, j in cnt:
        if is_valid[i] and is_valid[j]:
            last_t = t

            w1, num1 = marble[i][2], marble[i][4]
            w2, num2 = marble[j][2], marble[j][4]

            if (w1 > w2) or (w1 == w2 and num1 > num2):
                is_valid[j] = False
            else:
                is_valid[i] = False
    print(int(last_t) if last_t != -1 else -1)