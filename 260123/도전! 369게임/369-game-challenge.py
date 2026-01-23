import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N = input().strip()

dp = {} # key: (idx, rem, is_tight, is_start), value: 경우의 수

candidates = [0, 1, 2, 4, 5, 7, 8]
MOD = 10**9 + 7

# rem : 지금까지의 3으로 나눈 나머지
def solve(idx, rem, is_tight, is_start):
    if idx == len(N):
        # 숫자 존재 & 3배수 아님
        if is_start and rem != 0:
            return 1
        return 0

    cur = (idx, rem, is_tight, is_start)
    if cur in dp:
        return dp[cur]

    if is_tight:
        limit = int(N[idx])
    else:
        limit = 9

    cnt = 0
    for num in candidates:
        if num > limit:
            break

        n_tight = is_tight and num == limit
        n_start = is_start or num != 0
        if not n_start:
            n_rem = 0
        else:
            n_rem = (rem + num) % 3
        
        cnt = (cnt + solve(idx+1, n_rem, n_tight, n_start)) % MOD

    dp[cur] = cnt
    return cnt

# 숫자 줄이기, 기억해놓기
result = 0
for ch in N:
    result = (result * 10 + int(ch)) % MOD
no_clap = solve(0, 0, True, False)
print((result - no_clap + MOD) % MOD)