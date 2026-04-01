N = int(input()) # 참가자 수
size = list(map(int, input().split())) # 티셔츠 신청자수
T, P = map(int, input().split()) # 묶음 수

cntT = 0
for i in range(len(size)):
    if size[i] % T != 0:
        cntT += size[i] // T + 1
    else:
        cntT += size[i] // T

"""
# 티셔츠를 T장씩 최소 묶음으로 주문해야 하는 수 계산
cntT = sum((s + T - 1) // T for s in size)
s + (T - 1) <- 나눗셈 수행 시 == s / T에 나머지 올림한 것과 같음

Q ] 왜 올림되는가
A ] 이해함! T -1 을 더함으로써 2가지 case에 대해서 생각해보면됨
1. 만약 나누어떨어진다면
    이미 나누어떨어진 상태이기 때문에 T보다 작은 값을 더하여도 몫에는 변화가 없음.
    but T보다 같거나 큰 값을 더하면 변함
2. 만약 나누어떨어지지 않는다면
    이 경우가 진짜 올림이 필요한 경우임
    따라서 몫+1이 되기 위해 T와 한 번 더 나눌 수 있도록 피제수값+1이 되어야함
    => 따라서 (T-1)을 더하게 되면 나누어떨어지지않는 모든 피제수들이 +1됨
1 에서 요구 조건 -> T보다 작아야함
2 에서 요구 조건 -> T-1보다 크거나 같아야함
=> T-1

# 펜을 P자루씩 최대 몇 묶음과 한 자루씩 몇 개 주문하는지 계산
pen_bundles, pen_individuals = divmod(N, P)
"""        

print(cntT)
print(N//P, N%P)