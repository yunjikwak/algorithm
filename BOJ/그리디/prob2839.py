N = int(input())

n = 0

if N % 5 == 0: # 5로 나눠지는지 검사
    print(N // 5)
else:
    i = N // 5 # 5로 나눠지는 최대 몫
    while i >= 0:
        target = 5 * i
        if (N-target) % 3 == 0: # 나머지가 3으로 나눠지는가
            n = i + (N-target) // 3
            break
        i -= 1 # 하나씩 줄여가면서 검사
        
    if n == 0:
        print(-1) # 무리
    else:
        print(n)