### check
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sortA = sorted(A)

sum = 0
for i in range(N):
    b = B.pop(max(B).index)
    sum += sortA[i]*b
print(sum)