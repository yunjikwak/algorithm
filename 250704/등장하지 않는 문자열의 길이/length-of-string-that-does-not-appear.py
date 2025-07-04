import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip())

result = 0
for i in range(N): # 연속 개수 
    isSame = False
    L = i+1
    for j in range(len(arr)-L+1): # 시작 위치
        word = arr[j:j+L]
        for k in range(len(arr)):
            if k == j or (k < j and k+i > j) or (k > j and k < j+i): # j 범위 포함 X
                continue
            else:
                check = arr[k:k+i+1]
                if check == word: # 두 번 이상이면
                    isSame = True
                    break
        if isSame: # 이미 이 길이의 문자열에서 두 번 이상이면 더 이상 탐색 필요 X
            break
    
    if not isSame: # 전체 다 탐색해도 두 번 이상 X
        result = i+1
        break

print(result)