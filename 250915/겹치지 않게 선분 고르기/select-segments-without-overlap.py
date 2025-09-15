N = int(input())

line = []
for _ in range(N):
    line.append((list(map(int, input().split()))))

result = 0
store = []

def recur(num):
    global result

    if len(store) >= 2:
        nl, nr = line[store[-1]]
        ok = True
        for i in range(len(store)-1):
            a, b = line[store[i]]

            # 겹치지 않는 경우
                # nl이 b보다 크거나
                # nr이 a보다 작음
            if nl > b or nr < a:
                continue
            else:
                ok = False
                break
        if not ok:
            return

    if num == N:
        # print(store)
        result = max(result, len(store))
        return
    
    for select in range(num, len(line)):
        # print("select", select, num)
        store.append(select)
        recur(select+1)
        store.pop()

    return

recur(0)
print(result)