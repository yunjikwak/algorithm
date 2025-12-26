K, N = map(int, input().split())
answer = []

def print_answer():
    for ele in answer:
        print(ele, end=" ")
    print()

def select(cur):
    if cur == N:
        print_answer()
        return
    
    for i in range(1, K+1):
        answer.append(i)
        select(cur+1)
        answer.pop()
    return

select(0)