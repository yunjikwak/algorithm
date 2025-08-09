import sys
input = sys.stdin.readline

A = list(input().strip())

result = sys.maxsize
for i in range(len(A)):
    arr = A[-i:] + A[:-i]
    cnt = 1
    word = ''
    for j in range(1, len(arr)):
        if arr[j] == arr[j-1]:
            cnt += 1
        else:
            word += arr[j-1] + str(cnt)
            cnt = 1
    word += arr[-1] + str(cnt)
    result = min(result, len(word))
print(result)