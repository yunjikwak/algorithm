N = int(input())
result = set()

for idx in range(N):
    cur, first, second = map(int, input().split())
    cur = str(cur)

    tmp = set()

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if i == j  and j == k and k == i:
                    continue
                
                cnt1, cnt2 = 0, 0
                if i == int(cur[0]):
                    cnt1 += 1
                elif i == int(cur[1]) or i == int(cur[2]):
                    cnt2 += 1
                if j == int(cur[1]):
                    cnt1 += 1
                elif j == int(cur[0]) or j == int(cur[2]):
                    cnt2 += 1
                if k == int(cur[2]):
                    cnt1 += 1
                elif k == int(cur[0]) or k == int(cur[1]):
                    cnt2 += 1

                if cnt1 == first and cnt2 == second:
                    total = i*100 + j*10 + k
                    tmp.add(total)

    if idx == 0:
        result = tmp
    else:
        result &= tmp

print(len(result))