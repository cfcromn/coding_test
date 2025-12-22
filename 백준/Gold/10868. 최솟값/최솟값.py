import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
Mintree = [0] * (4 * len(arr))
INT = 10 ** 15

def buildMinTree(start, end, node):
    if start == end:
        Mintree[node] = arr[start]
        return Mintree[node]
    mid = (start + end) // 2
    Mintree[node] = min(buildMinTree(start, mid, node * 2), buildMinTree(mid + 1, end, node * 2 + 1))
    return Mintree[node]

def queryMin(start, end, node, left, right):
    if right < start or end < left:
        return INT

    if left <= start and end <= right:
        return Mintree[node]

    mid = (start + end) // 2
    return min(queryMin(start, mid, node * 2, left, right), queryMin(mid + 1, end, node * 2 + 1, left, right))
    
buildMinTree(0, len(arr) - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    minNum = queryMin(0, len(arr) - 1, 1, a - 1, b - 1)
    print(minNum)