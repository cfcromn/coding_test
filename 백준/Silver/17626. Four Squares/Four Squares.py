import sys
import math
input = sys.stdin.readline

n = int(input())
cnt = 0

def f(n):
    while n % 4 == 0:
        n = n // 4
    if n % 8 == 7:
        return True
    return False

def t(n):
    for i in range(1, math.isqrt(n) + 1):
        rest = n - i ** 2
        t = math.isqrt(rest)
        if rest == t*t:
            return True
    return False


if n - math.isqrt(n) ** 2 == 0:
    print(1)
elif f(n):
    print(4)
elif t(n):
    print(2)
else:
    print(3)