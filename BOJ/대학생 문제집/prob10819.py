N = int(input())
A = list(map(int, input().split()))

arr = []
result = 0
check = [False] * N

def find():
    global result, arr
    
    if len(arr) == N:
        tmp = 0
        for i in range(len(arr)-1):
            tmp += abs(arr[i] - arr[i+1])
        if tmp > result:
            result = tmp
            # print(arr, end=' ')
            # print(tmp)
        return
    
    for i in range(len(A)):
        # if i not in arr:
        #     arr.append(i)
        #     find()
        #     arr.pop()
        if not check[i]:
            check[i] = True
            arr.append(A[i])
            find()
            arr.pop()
            check[i] = False
    
find()
print(result)