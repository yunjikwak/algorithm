T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    
    result = []
    for i in S:
        for j in range(R):
            result.append(i)
    print(''.join(result))