import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bomb = [int(input()) for _ in range(N)]

def explosion(start, end):
    for i in range(start, end+1):
        bomb[i] = 0

def calc():
    global bomb
    tmp = []
    for b in bomb:
        if b != 0:
            tmp.append(b)
    bomb = tmp


bomb_cnt = -1
while True:
    cnt = 1
    length = len(bomb)

    if bomb_cnt == 0:
        break
    else:
        bomb_cnt = 0

    for i in range(1, length):
        if bomb[i-1] == bomb[i]:
            cnt += 1
            continue
        elif cnt >= M:
            bomb_cnt += 1
            explosion(i-cnt, i-1)
        cnt = 1
    if cnt >= M:
        bomb_cnt += 1
        explosion(length-cnt, length-1)
    calc()

print(len(bomb))
for b in bomb:
    print(b)
