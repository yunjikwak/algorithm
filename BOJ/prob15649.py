N, M = map(int, input().split())
include = []

def perm():
    if len(include) == M:
        for i in range(M):
            print(include[i], end=' ')
        print("")
        return
    for i in range(1, N+1):
        if i not in include:
            include.append(i)
            perm()
            include.pop() # 큰 수가 앞으로 나오게 해줌
            
perm()