import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visited[v] = True
    cnt = 0
    for i in range(1, n + 1):
        if graph[v][i] == 1 and visited[i] == False:
            cnt += 1
            cnt += dfs(i)
    return cnt

print(dfs(1))