T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 문서 개수, 알아낼 문서
    arr = list(map(int, input().split()))
    arr = [(i, arr[i]) for i in range(N)]
    
    point = 0
    while point < N:
        if arr[point][1] == max(arr[point:], key = lambda x:x[1])[1]:
            point += 1
        else:
            tmp = arr[point]
            arr.remove(arr[point])
            arr.append(tmp)
    result = 1
    for i in range(N):
        if arr[i][0] == M:
            print(result)
            break
        else:
            result += 1