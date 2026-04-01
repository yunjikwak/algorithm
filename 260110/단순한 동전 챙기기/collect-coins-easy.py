N = int(input())

arr = []
coin = [[] for _ in range(11)]
for i in range(N):
    row = list(map(int, input().strip()))
    for j in range(len(row)):
        if row[j] == 'S':
            coin[0] = (i, j)
        elif row[j] == 'E':
            coin[10] = (i, j)
        elif row[j] == '.':
            continue
        else:
            coin[int(row[j])] = (i, j)
    arr.append(row)


