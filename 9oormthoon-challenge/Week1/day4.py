N = int(input())
K = list(map(int, input().split()))
	
mid = K.index(max(K))

result = K[mid]
i, j = mid, mid
while True:
	if i == 0 or j == N-1:
		break
	
	if K[i-1] > K[i] or K[j+1] > K[j]:
		print('0')
		exit()
	
	i -= 1
	j += 1
	result += K[i]+K[j]
	
while i != 0:
		if K[i-1] > K[i]:
			print('0')
			exit()
		i -= 1
		result += K[i]
		
while j != N-1:
		if K[j+1] > K[j]:
			print('0')
			exit()
		j += 1
		result += K[j]

print(result)