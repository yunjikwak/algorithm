N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0


def check_color(x, y, size):
    global white, blue
    color = square[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if square[i][j] != color:
                check_color(x, y, size//2)
                check_color(x + size//2, y, size//2)
                check_color(x, y + size//2, size//2)
                check_color(x + size//2, y + size//2, size//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1


check_color(0, 0, N)
print(white)
print(blue)
