A = input()
B = input()

# print(len(A), len(B))

# indexError
c = [[0] * (len(B)+1) for _ in range(len(A)+1)] 

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if (A[i-1] == B[j-1]):
            c[i][j] = c[i-1][j-1] + 1
        else:
            c[i][j] = max(c[i-1][j],  c[i][j-1])

print(c[-1][-1])