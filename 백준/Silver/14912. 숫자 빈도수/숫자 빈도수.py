import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    strI = str(i)
    cnt += strI.count(str(m))
print(cnt)