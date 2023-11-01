import sys
input = sys.stdin.readline

N = int(input())

stack = []

def push(n):
    stack.append(n)
def pop():
    if len(stack) == 0:
        return -1
    return stack.pop()
def size():
    return len(stack)
def empty():
    if len(stack) == 0:
        return 1
    return 0
def top():
    if len(stack) == 0:
        return -1
    return stack[-1]

for _ in range(N):
    a = input().split()
    if a[0] == 'push':
        push(int(a[1]))
    elif a[0] == 'pop':
        print(pop())
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'empty':
        print(empty())
    elif a[0] == 'top':
        print(top())