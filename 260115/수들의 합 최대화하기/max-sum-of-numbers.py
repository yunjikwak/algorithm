N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited_c = [False] * N

result = 0
def choose(row, cur):
    global result

    if row == N:
        result = max(result, cur)
        return

    for j in range(N):
        if not visited_c[j]:
            visited_c[j] = True
            choose(row + 1, cur + arr[row][j])
            visited_c[j] = False

choose(0, 0)
print(result)