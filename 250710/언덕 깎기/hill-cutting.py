import sys
input = sys.stdin.readline

N = int(input())
H = list(int(input()) for _ in range(N))

start = min(H)
end = max(H)

cost = sys.maxsize
for h in range(start, end+1):
    cur_cost = 0
    for hill in H:
        dif = 0
        if hill < h:
            dif = h - hill
        elif hill >= h and hill <= h+17:
            continue
        elif hill > h+17:
            dif = h+17-hill
        cur_cost += dif * dif
    cost = min(cost, cur_cost)
        
print(cost)