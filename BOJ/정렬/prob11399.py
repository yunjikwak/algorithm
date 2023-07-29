N = int(input())
P = list(map(int, input().split()))

P.sort()

sum_list = [0] * N
sum_list[0] = P[0]
for i in range(1, len(P)) :
    sum_list[i] = sum_list[i-1] + P[i]

result = sum(sum_list)
print(result)