K, N = map(int, input().split())

answer = []

def print_answer():
    for ele in answer:
        print(ele, end=' ')
    print()

def choose(curr_num):
    if curr_num == N:
        print_answer()
        return
    
    for i in range(1, K + 1):
        if curr_num >= 2:
            if answer[-1] == i and answer[-2] == i:
                continue
        
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

    return

choose(0)