import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

end = max(arr)
for i in range(1, end):
    tmp = [0] * N
    tmp[0] = i
    for j in range(len(arr)): # 임시로 계산하기
        tmp[j+1] = abs(arr[j] - tmp[j])

    check = True # 조건 만족 수열 검사
    check_lst = [0] * (N + 1)
    for num in tmp:
        if not (1 <= num <= N) or check_lst[num] == 1:
            check = False
            break
        check_lst[num] = 1
    
    if check:
        print(*tmp)
        break