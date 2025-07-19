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
        candidate.append((gap + 1) // 2)

print(min(sorted(candidate, reverse=True)[:2])) # 홀 짝 고려