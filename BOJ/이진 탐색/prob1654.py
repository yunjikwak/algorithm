K, N = map(int, input().split()) # K개 랜선, N개 같은 길이
arr = []

for i in range(K) :
    arr.append(int(input()))
arr.sort()

start = 1
end = max(arr) # 모두 동일 길이

# result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in arr:
        total += x // mid
        
    if total < N:
        end = mid - 1
    else:
        # result = mid
        start = mid + 1

print(end)