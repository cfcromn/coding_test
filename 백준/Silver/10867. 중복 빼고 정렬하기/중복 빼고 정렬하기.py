import sys
input = sys.stdin.readline

n = int(input())
num = map(int, input().split())

set_list = sorted(list(set(num)))
for i in range(len(set_list)):
    print(set_list[i], end = " ")