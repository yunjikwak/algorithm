N, K = map(int, input().split())

arr = []
result = []
for i in range(1, N+1):
    arr.append(i)
    
now = 0
while arr:
    now = (now + K - 1) % len(arr)
    result.append(arr.pop(now))
        
formatted_list = "<" + ", ".join(map(str, result)) + ">"
print(formatted_list)