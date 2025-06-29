import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
start = min(arr)
end = max(arr)

result = 0
for k in range(start+1, end):
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            a, b = arr[i], arr[j]
            if a - k == k - b:
                cnt += 1
                break
    
    result = max(result, cnt)
print(result)