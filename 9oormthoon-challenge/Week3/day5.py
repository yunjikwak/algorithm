N, K = map(int, input().split())

arr = list()
for _ in range(N):
	P, C = map(int, input().split())
	arr.append((P, C))
	
arr.sort(key=lambda x: x[1] // x[0], reverse=True)

result = 0
for P, C in arr:
	if K >= P:
		result += C
		K -= P
	else:
		result += (K * (C // P))
		break
print(result)