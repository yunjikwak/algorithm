N = int(input())
a, b, c = map(int, input().split())

answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if a-2 <= i <= a + 2 or b-2 <= j <= b + 2 or c-2 <= k <= c + 2:
                answer += 1
print(answer)
