N, M = map(int, input().split()) # 한 줄에 입력받기
include = []

def perm(k):
    if len(include) == M:
        for i in range(M):
            print(include[i], end=' ')
        print("") #\n 쓰지 않아도 됨
        return
    for i in range(k, N+1):
        if i not in include:
            include.append(i)
            perm(i+1) # k+1 아님~! k랑 i 구분하기!!
            include.pop()
            
perm(1)