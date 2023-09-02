N, K = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in range(len(a)):
	b.append((bin(a[i])[2:].count('1'), a[i]))

b.sort(key=lambda x: (-x[0], -x[1])) # 람다 사용 방법 까먹지 말기!!!
# (+) 내림차순 정렬 시 - 사용 

print(b[K-1][1])