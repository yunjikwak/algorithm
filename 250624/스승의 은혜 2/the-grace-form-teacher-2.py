import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

max_student = 0
for i in range(N):
    cost = 0
    student = 0
    for j in range(N):
        if i == j:
            if cost + arr[i] // 2 > B:
                break
            else:
                cost += arr[i] // 2
                student += 1
        elif cost + arr[j] > B:
            break
        else:
            cost += arr[j]
            student += 1
    max_student = max(max_student, student)

print(max_student)