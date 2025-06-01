N, T = map(int, input().split())
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # N W S E
move_dir = 0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

string = list(input().strip())

maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

sum = 0
x, y = N // 2, N // 2
sum += maps[x][y]

for command in string:
    if command == 'F':
        nx, ny = x + dx[move_dir], y + dy[move_dir]
        if not in_range(nx, ny):
            continue
        else:
            x, y = nx, ny
            sum += maps[x][y]
    elif command == 'L':
        move_dir = (move_dir+1)%4
    elif command == 'R':
        move_dir = (move_dir+3)%4
print(sum)