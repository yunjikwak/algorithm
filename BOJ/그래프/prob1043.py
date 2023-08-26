N, M = map(int, input().split())
truth = list(map(int, input().split()))
truth_num = truth[0]
truth = set(truth[1:])

party_all = []
for _ in range(M):
    party = list(map(int, input().split()))
    party_all.append(party[1:])

# for party in party_all:
#     check = False
#     for i in party:
#         if i in truth:
#             check = True
#             break
#     if check:
#         truth.extend(party)
# truth = set(truth)
# truth = list(truth)

for _ in range(M):
    for party in party_all:
        if any(p in truth for p in party):
            truth.update(party)

cnt = 0

for party in party_all:
    contain = False
    for i in party:
        if i in truth:
            contain = True
            break
    if contain == False:
        cnt+= 1

# for party in party_all:
#     if all(p not in truth for p in party):
#         cnt += 1
        
print(cnt)