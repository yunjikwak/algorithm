import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cost = 0
move = 0
for i in range(N):
    cost += move
    a = A[i]
    b = B[i]

    if a < b:
        move -= b-a
    else:
        move += a-b
print(cost)