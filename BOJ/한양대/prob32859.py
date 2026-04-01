N, M = map(int, input().split())
S = int(input())

events = []
for _ in range(M):
    i, t = map(int, input().split())
    events.append((i, t))

form = {}
money = []
forget = []

for idx, (i,t) in enumerate(events):
    if t == 0:
        form[i] = idx
    elif t == 1:
        if i in form:
            continue
        money.append((i, idx))

for i, timing in money:
    cnt = 0
    for j in range(timing+1, M):
        a, b = events[j]
        if b != 0:
            continue
        if a == i and b == 0:
            break
        cnt += 1

        if cnt >= S:
            forget.append(i)
            break

# for i in range(1, N+1):
#     if i in form or i in forget or i in dict(money):
#         continue
#     forget.append(i)

forget.sort()
if len(forget) == 0:
    print(-1)
else:
    for i in forget:
        print(i)