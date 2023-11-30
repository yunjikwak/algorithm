import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        a, b = map(int, input().split())
        score.append(list((a,b)))
    score.sort(key=lambda x: (x[0], x[1]))
    # score.sort(key=lambda x:x[0])
    
    num = 1
    cur_min = score[0][1]
    for i in range(1, N):
        if score[i][1] < cur_min:
            cur_min = score[i][1]
            num += 1
    print(num)