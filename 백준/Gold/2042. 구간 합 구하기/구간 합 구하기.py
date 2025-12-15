import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
tree = [0] * (4 * len(arr))

def init(start, end, node):
    if start == end:
        tree[node] = arr[start] 
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def update(start, end, node, idx, value):
    if start == end:
        arr[idx] = value 
        tree[node] = value 
        return

    mid = (start + end) // 2
    if idx <= mid:
        update(start, mid, node * 2, idx, value)
    else:
        update(mid + 1, end, node * 2 + 1, idx, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(start, end, node, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right) 
    
    
init(0, len(arr) - 1, 1)
for _ in range(k+m):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0,len(arr)-1,1,b-1,c)
    elif a == 2:
        print(query(0, len(arr) - 1, 1, b - 1, c - 1))
