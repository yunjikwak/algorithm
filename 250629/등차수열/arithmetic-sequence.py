import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        a, b = arr[i], arr[j]
        start = min(a,b)
        end = max(a,b)
        for k in range(start+1, end):
            if a - k == k - b:
                result += 1
                break
print(result)