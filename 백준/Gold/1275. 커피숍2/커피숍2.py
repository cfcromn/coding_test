import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (4 * len(arr))

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

def update(start, end, node, index, value):
    if start == end:
        arr[index] = value
        tree[node] = value
        return
        
    mid = (start + end) // 2
    if index <= mid:
        update(start, mid, node * 2, index, value)
    else:
        update(mid + 1, end, node * 2 + 1, index, value)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(start, end, node, left, right):
    if right < start or end < left:
        return 0
    
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right) 

init(0, len(arr) - 1, 1)
out = []
for _ in range(q):
    x, y, a, b = map(int, input().split())
    l = min(x, y) - 1
    r = max(x, y) - 1
    out.append(str(query(0, n - 1, 1, l, r)))
    update(0, n - 1, 1, a - 1, b)
sys.stdout.write("\n".join(out))