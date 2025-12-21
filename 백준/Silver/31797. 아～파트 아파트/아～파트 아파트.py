import sys
input = sys.stdin.readline

n, m = map(int, input().split())

items = []
for i in range(1, m + 1):
    a, b = map(int, input().split())
    items.append((a, i))
    items.append((b, i))

items.sort()

n %= (2 * m)
if n == 0:
    n = 2 * m

print(items[n - 1][1])
