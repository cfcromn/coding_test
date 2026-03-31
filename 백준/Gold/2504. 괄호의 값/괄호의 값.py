import sys
input = sys.stdin.readline

s = input().strip()
stack = []

for ch in s:
    if ch == '(' or ch == '[':
        stack.append(ch)

    elif ch == ')':
        if not stack:
            print(0)
            sys.exit()

        temp = 0
        while stack and stack[-1] != '(':
            if stack[-1] == '[':
                print(0)
                sys.exit()
            temp += stack.pop()

        if not stack:
            print(0)
            sys.exit()

        stack.pop()

        if temp == 0:
            stack.append(2)
        else:
            stack.append(temp * 2)

    elif ch == ']':
        if not stack:
            print(0)
            sys.exit()

        temp = 0
        while stack and stack[-1] != '[':
            if stack[-1] == '(':
                print(0)
                sys.exit()
            temp += stack.pop()

        if not stack:
            print(0)
            sys.exit()

        stack.pop() 

        if temp == 0:
            stack.append(3)
        else:
            stack.append(temp * 3)

answer = 0
for x in stack:
    if x == '(' or x == '[':
        print(0)
        sys.exit()
    answer += x

print(answer)