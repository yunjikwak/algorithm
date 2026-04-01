N, M, K = map(int, input().split())
num = list(map(int, input().split()))

answer = [1] * K
val = 0

def calc(arr):
    cnt = 0
    for ele in arr:
        if ele >= M:
            cnt += 1
    return cnt

def choose(curr_num):
    global val

    if curr_num == N:
        cur = calc(answer)
        val = max(val, cur)
        return

    for i in range(K):
        answer[i] += num[curr_num]
        choose(curr_num + 1)
        answer[i] -= num[curr_num]
    return

choose(0)
print(val)