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
    
    # t초 후 좌표가 같은 경우
        # nx = x1 + v * t
        # x1 + v1*t = x2 + v2*t
        # t = (x2 - x1) / (vx1 - vx2)

    if vx1 == vx2:
        tx = None
    else:
        tx = (x2 - x1) / (vx1 - vx2)
    if vy1 == vy2:
        ty = None
    else:
        ty = (y2 - y1) / (vy1 - vy2)

    if tx is None: # x축 이동 동일
        t = ty
    elif ty is None:
        t = tx
    elif tx == ty:
        t = tx
    else:
        return None

    if t <= 0:
        return None

    return t

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
    idx = 0
    while idx < len(cnt):
        t = cnt[idx][0]
        cur = []

        while idx < len(cnt) and cnt[idx][0] == t:
            cur.append(cnt[idx])
            idx += 1

        involved = set()
        for _, i, j in cur:
            if is_valid[i] and is_valid[j]:
                involved.add(i)
                involved.add(j)

        if not involved:
            continue

        involved = list(involved)
        involved.sort(key=lambda k: (marble[k][2], marble[k][4])) 
        survivor = involved[-1]

        for k in involved:
            if k != survivor:
                is_valid[k] = False

        last_t = T
        
    print(int(last_t) if last_t != -1 else -1)