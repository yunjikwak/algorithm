N = int(input())
arr = list(map(int, input().split()))

list_sort = sorted(set(arr))

def binary_search(target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if list_sort[mid] == target:
        return mid
    elif list_sort[mid] > target:
        return binary_search(target, start, mid-1)
    else:
        return binary_search(target, mid+1, end)
        

result = []
for i in range(N):
    result.append(binary_search(arr[i],0,len(list_sort)))
    
print(*result)