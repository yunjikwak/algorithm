from collections import deque
import sys
input = sys.stdin.readline

q = deque()
N = int(input())

def execute(command):
    word = command[0]
    if word == "push_front":
        q.appendleft(int(command[1]))
    elif word == "push_back":
        q.append(int(command[1]))
    elif word == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif word == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif word == "size":
        print(len(q))
    elif word == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif word == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif word == "back":
        if q:
            print(q[-1])
        else:
            print(-1)

for _ in range(N):
    command = input().split()
    execute(command)