import sys

input = sys.stdin.readline
a, b = map(int, input().split())

def minus(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    return max_num - min_num

print(minus(a, b))