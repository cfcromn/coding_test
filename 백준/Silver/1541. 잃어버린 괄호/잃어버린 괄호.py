import sys
input = sys.stdin.readline

s = input().strip()
s = s.replace('-', ' - ')
s = s.replace('+', ' + ')
s = s.split()

mt = []
t = []
cnt = 0
check = 1
for i in range(len(s)):
    if len(s) == 1:
        t.append(int(s[i]))
        break
    if cnt == check:
        t.append(-1 * sum(mt))
        mt = []
        check += 1
    if s[i] == '-':
        cnt += 1
    elif s[i] == '+':
        continue
    elif cnt > 0:
        mt.append(int(s[i]))
    else:
        t.append(int(s[i]))
if mt:
    t.append(-1 * sum(mt))
print(sum(t))