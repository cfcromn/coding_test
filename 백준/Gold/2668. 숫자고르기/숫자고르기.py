import sys
input = sys.stdin.readline

n = int(input())
num = [0] + [int(input()) for _ in range(n)]
result = []
visited = [False] * (n + 1)
onPath = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    onPath[v] = True
    next = num[v]
    if not visited[next]:
        dfs(next)
    elif onPath[next]:
        cur = next
        while True:
            result.append(cur)
            cur = num[cur]
            if cur == next:
                break
    onPath[v] = False

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
print(len(result))
result = sorted(result)
for i in range(len(result)):
    print(result[i])