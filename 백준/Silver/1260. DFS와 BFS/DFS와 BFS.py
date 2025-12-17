import sys
from collections import deque
input = sys.stdin.readline


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n+1)]
visitedDfs = [False] * (n + 1)
visitedBfs = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    visitedDfs[v] = True
    print(v, end = " ")
    for i in range(1, n+1):
        if graph[v][i] == 1 and visitedDfs[i] == False:
            # print(visitedDfs)
            dfs(i)

def bfs(v):
    visitedBfs[v] = True
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if(visitedBfs[i] == 0 and graph[v][i] == 1):
                q.append(i)
                visitedBfs[i] = True

dfs(v)
print()
bfs(v)