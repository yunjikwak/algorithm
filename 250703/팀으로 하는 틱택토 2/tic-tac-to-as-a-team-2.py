import sys
input = sys.stdin.readline

arr = [list(map(int, input().strip())) for _ in range(3)]
result = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue

        check = False
        a, b = str(i), str(j)
        can = [a+a+b, a+b+a, b+a+a]

        x_list = ["".join(map(str, row)) for row in arr]
        for x in range(3):
            if x_list[x] in can:
                check = True
                continue
        
        if not check:
            for col in range(3):
                temp = []
                for row in range(3):
                    temp.append(str(arr[row][col]))
                y = "".join(temp)
            
                if y in can:
                    check = True
                    continue
        
        if not check:
            diag1 = "".join([str(arr[i][i]) for i in range(3)])
            diag2 = "".join([str(arr[i][2-i]) for i in range(3)])
            if diag1 in can or diag2 in can:
                check = True
        
        if check:
            result += 1

print(result)
