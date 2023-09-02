T = int(input())

result = 0
for _ in range(T):
	a, b, c = input().split()
	a = int(a)
	c = int(c)
	
	tmp = 0
	if b == '+':
		tmp = a+c
	elif b == '-':
		tmp = a-c
	elif b == '*':
		tmp = a*c
	elif b == '/':
		tmp = a // c
	
	result += tmp

print(result)