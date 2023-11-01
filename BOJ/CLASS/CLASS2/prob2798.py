N, M = map(int, input().split())
card = list(map(int, input().split()))

sumThree = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = card[i] + card[j] + card[k]
            if sumThree < tmp <= M :
                sumThree = tmp

print(sumThree)