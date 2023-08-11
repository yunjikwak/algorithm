N, K = map(int, input().split())
arr = []

for i in range(N):
    w, v = map(int, input().split())
    arr.append([w,v])
    
# dp(i,w) : 배낭 용량이 w일 때 아이템 1~i로 얻을 수 있는 최대 이득
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        # arr랑 idx가 하나씩 느려서 i-1로 해야 타겟이 매칭됨
        w = arr[i-1][0] # 현재 타겟의 무게
        v = arr[i-1][1] # 비용
        
        if w > j : # 선택 시 용량 초과임
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
            
print(dp[N][K])