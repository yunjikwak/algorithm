import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

canA = []
canB = []
for i in arr1:
    lst = []
    for k in range(-2, 2+1):
        lst.append((i + k - 1) % N + 1)
    canA.append(lst)
for j in arr2:
    lst = []
    for k in range(-2, 2+1):
        lst.append((j + k - 1) % N + 1)
    canB.append(lst)

result = len(canA[0]) * len(canA[1]) * len(canA[2])
result += len(canB[0]) * len(canB[1]) * len(canB[2])

minus = []
for i in range(3):
    tmp = 0
    for j in range(len(canB[i])):
        if canB[i][j] in canA[i]:
            tmp += 1
    minus.append(tmp)

result -= minus[0] * minus[1] * minus[2]
print(result)