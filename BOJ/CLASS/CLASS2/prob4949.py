stack = []

string = input()
while string[0] != '.':
    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) < 1:
                print("no")
                break
            if stack.pop() == '(':
                continue
            else:
                print("no")
                break
        elif c == ']':
            if len(stack) < 1:
                print("no")
                break
            if stack.pop() == '[':
                continue
            else:
                print('no')
                break
        elif c == '.':
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
            break
    stack.clear()
    string = input()