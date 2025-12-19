import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bt = []
lst = list(map(int, input().split()))
sort_list = sorted(lst)
visited = [False] * n

def nm(depth):
    if depth == m:
        print(*bt)
        return
    for i in range(n):
        if visited[i]:
            continue

        bt.append(sort_list[i])
        visited[i] = True

        nm(depth + 1)

        bt.pop()
        visited[i] = False    

nm(0)