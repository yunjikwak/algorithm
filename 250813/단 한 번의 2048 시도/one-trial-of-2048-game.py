import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]
d = input().strip()

def short(a):
    tmp = []
    for i in range(len(a)):
        if a[i] != 0:
            tmp.append(a[i])
    return tmp

def calc_arr(a, reverse=False):
    a = short(a)
    if reverse:
        a = a[::-1]

    store = []
    jump = False
    for i in range(len(a)):
        if jump:
            jump = False
            continue
        if i < len(a) - 1 and a[i] == a[i+1]:
            store.append(a[i] + a[i])
            jump = True
        else:
            store.append(a[i])

    while len(store) < 4:
        store.append(0)

    if reverse:
        store = store[::-1]
    return store

if d == 'L':
    for i in range(4):
        arr[i] = calc_arr(arr[i], reverse=False)
elif d == 'R':
    for i in range(4):
        arr[i] = calc_arr(arr[i], reverse=True)
elif d == 'U':
    for i in range(4):
        store = []
        for j in range(4):
            store.append(arr[j][i])
        col = calc_arr(store, reverse=False)

        for j in range(4):
            arr[j][i] = col[j]
elif d == 'D':
    for i in range(4):
        store = []
        for j in range(4):
            store.append(arr[j][i])
        col = calc_arr(store, reverse=True)

        for j in range(4):
            arr[j][i] = col[j]

for row in arr:
    print(*row)