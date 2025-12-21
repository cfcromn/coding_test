import sys
input = sys.stdin.readline

s = input().strip()
lst = []
for i in range(len(s)):
    lst.append(s[i:])
lst = sorted(lst)
for i in range(len(lst)):
    print(lst[i])