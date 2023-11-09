# 랭킹 리스트에 올라갈 수 있는 점수 개수 P
# 새로운 점수가 몇 등
N, score, P = map(int, input().split())
if N == 0:
    print(1)
    exit()
else:
    score_board = list(map(int, input().split()))
score_board = sorted(score_board, reverse=True)

result = -1
idx = 0
equal = -1

for idx, i in enumerate(score_board):
    if idx > P-1: # 점수판 기록 가능 넘음
        break
    if i == score: # 점수가 같음
        if equal == -1: equal = idx # 동일 등수 저장
        if idx != len(score_board) - 1:
            if score_board[idx+1] != score:
                result = equal + 1
                break
        elif idx < P - 1:
            result = equal + 1
            break
        continue
    if i < score:
        result = idx+1
        break

if idx < P-1 and result == -1:
    result = len(score_board) + 1
    
print(result)

"""
4 1 4
5 4 3 2
-> -1

1 0 10
1
-> 2

11 500 10
600 600 600 600 600 600 600 600 600 600 400
-> -1

10 1 11
1 1 1 1 1 1 1 1 1 1
-> 1

12 100 10
100 100 100 100 100 100 100 100 100 90 90 90
-> 1

10 0 11
10 9 8 7 6 5 4 3 2 1
-> 11

10 1 10
1 1 1 1 1 1 1 1 1 1
-> -1
"""