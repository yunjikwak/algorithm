## 다시 풀어서 혼자 이해해보기

N, M = map(int, input().split())

result = 1

if N <= 1 :
    result = 1
elif N == 2 :
    result = min(4, (M+1)//2)
elif M < 7:
    result = min(4, M)
else:
    result = 5 + M - 7

print(result)