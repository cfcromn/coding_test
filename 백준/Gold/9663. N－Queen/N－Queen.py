import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * (n + 1) for _ in range(n)]
col = [False] * n
d1 = [False] * (2*n-1)
d2 = [False] * (2*n-1)
cnt = 0

def dfs(depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    for i in range(n):
        if col[i] or d1[depth - i] or d2[depth + i]:
            continue
        board[depth][i] = 1
        col[i] = True
        d1[depth - i] = True
        d2[depth + i] = True

        dfs(depth + 1)

        board[depth][i] = 0
        col[i] = False
        d1[depth - i] = False
        d2[depth + i] = False

dfs(0)
print(cnt)