## ???????????????? 👍 해결 완!!!!!!!!!!

N, C = map(int, input().split())
arr = []

for i in range(N) :
    arr.append(int(input()))
    
arr.sort()

# start = arr[1] - arr[0] 
start = 1
end = max(arr) - arr[0]

result = 0
while(start <= end):
    cnt = 1
    mid = (start + end) // 2
    
    prev = arr[0]
    for x in arr :
        if x >= prev + mid :
            cnt += 1
            prev = x
            
    if cnt < C:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)