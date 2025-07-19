import sys
input = sys.stdin.readline

N = int(input())
seat = list(map(int, input().strip()))

can_pos = []
candidate = []

for idx, s in enumerate(seat):
    if s:
        can_pos.append(idx)

for i in range(len(can_pos) - 1):
    gap = can_pos[i+1] - can_pos[i] - 1
    if gap >= 1:
        mid = can_pos[i] + (gap + 1) // 2
        candidate.append(mid)

dis = 0

for pos in candidate:
    new_seat = seat[:]
    new_seat[pos] = 1

    cur_dis = len(new_seat)
    start = 0
    for i in range(1, len(new_seat)-1):
        if new_seat[i] == 0:
            continue
        elif new_seat[i] == 1:
            cur_dis = min(cur_dis, i-start)
            start = i

    dis = max(dis, cur_dis)

print(dis)