n = int(input())
arr = []
stack = []
for _ in range(n):
    arr.append(int(input()))
    
point = 0
result = []

for i in range(1,n+1):
    if i != arr[point]:
        result.append("+")
        stack.append(i)
    elif i == arr[point]:
        result.append("+")
        stack.append(i)
        
        while point < n and i >= arr[point] :
            result.append("-")
            tmp = stack.pop()
            if tmp != arr[point]:
                print("NO")
                exit()
            point += 1
print(*result, sep='\n')