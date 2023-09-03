N = int(input())
A, B = map(int, input().split())

MAX_N = 10**6 + 1 
d = [0] * MAX_N

for i in range(A, N+1):
	if i - B == 0:
		d[i] = 1
	elif i - A == 0:
		d[i] = 1
	
	if i - B > 0 and d[i-B] != 0:
		d[i] = d[i-B]+1
	if i - A > 0 and d[i-A] != 0:
		if d[i] != 0:
			d[i] = min(d[i], d[i-A]+1)
		else:
			d[i] = d[i-A]+1
	# print(i, d[i])
	
if d[N] == 0:
	print("-1")
else:
	print(d[N])