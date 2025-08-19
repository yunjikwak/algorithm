import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
curr_x, curr_y = r - 1, c - 1

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

result = [a[curr_x][curr_y]]

while True:
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    moved = False
    for dx, dy in zip(dxs, dys):
        next_x = curr_x + dx
        next_y = curr_y + dy

        if inRange(next_x, next_y) and a[next_x][next_y] > a[curr_x][curr_y]:
            curr_x, curr_y = next_x, next_y
            result.append(a[curr_x][curr_y])
            moved = True
            break

    if not moved:
        break

print(*result)