import sys
input = sys.stdin.readline

# 방향: U D L R
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for _ in range(T):
    N = int(input())

    OFFSET = 1000
    marble = []
    for i in range(N):
        x, y, w, d = input().split()
        x, y, w = int(x), int(y), int(w)
        if d == 'U': d = 0
        elif d == 'D': d = 1
        elif d == 'L': d = 2
        elif d == 'R': d = 3
        marble.append([2*(x+OFFSET), 2*(y+OFFSET), w, d, i])

    is_alive = [True]*N
    last_time = -1

    for t in range(1, 4*OFFSET+2*N):
        pos_map = dict()

        for idx, (x, y, w, d, num) in enumerate(marble):
            if not is_alive[idx]:
                continue
            nx, ny = x + dx[d], y + dy[d]
            marble[idx][0], marble[idx][1] = nx, ny
            if (nx, ny) not in pos_map:
                pos_map[(nx, ny)] = []
            pos_map[(nx, ny)].append(idx)

        for indices in pos_map.values():
            if len(indices) > 1:
                last_time = t
                indices.sort(key=lambda k: (marble[k][2], marble[k][4]), reverse=True)
                survivor = indices[0]
                for k in indices[1:]:
                    is_alive[k] = False

    print(last_time)
