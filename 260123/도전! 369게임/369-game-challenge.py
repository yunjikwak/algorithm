import sys

input = sys.stdin.readline
S = input().strip()
L = len(S)
MOD = 10**9 + 7

allowed = [0, 1, 2, 4, 5, 7, 8]

total_n_mod = 0
for ch in S:
    total_n_mod = (total_n_mod * 10 + int(ch)) % MOD

no_clap_count = 0

if L > 1:
    current_dp = [0, 3, 3] 
    
    no_clap_count = (no_clap_count + current_dp[1] + current_dp[2]) % MOD
    
    for _ in range(2, L):
        next_dp = [0, 0, 0]
        next_dp[0] = (current_dp[0]*1 + current_dp[1]*3 + current_dp[2]*3) % MOD
        next_dp[1] = (current_dp[0]*3 + current_dp[1]*1 + current_dp[2]*3) % MOD
        next_dp[2] = (current_dp[0]*3 + current_dp[1]*3 + current_dp[2]*1) % MOD
        
        current_dp = next_dp
        no_clap_count = (no_clap_count + current_dp[1] + current_dp[2]) % MOD

loose_dp = [0, 0, 0]

tight_rem = 0
tight_valid = True

for i in range(L):
    limit = int(S[i])
    next_loose_dp = [0, 0, 0]
    
    next_loose_dp[0] = (loose_dp[0]*1 + loose_dp[1]*3 + loose_dp[2]*3) % MOD
    next_loose_dp[1] = (loose_dp[0]*3 + loose_dp[1]*1 + loose_dp[2]*3) % MOD
    next_loose_dp[2] = (loose_dp[0]*3 + loose_dp[1]*3 + loose_dp[2]*1) % MOD
            
    if tight_valid:
        for digit in allowed:
            if digit >= limit:
                break 
            if i == 0 and digit == 0:
                continue
            
            new_rem = (tight_rem + digit) % 3
            next_loose_dp[new_rem] = (next_loose_dp[new_rem] + 1) % MOD
    
    loose_dp = next_loose_dp
    
    if limit in [3, 6, 9]:
        tight_valid = False
    else:
        tight_rem = (tight_rem + limit) % 3

no_clap_count = (no_clap_count + loose_dp[1] + loose_dp[2]) % MOD

if tight_valid and tight_rem != 0:
    no_clap_count = (no_clap_count + 1) % MOD

print((total_n_mod - no_clap_count + MOD) % MOD)