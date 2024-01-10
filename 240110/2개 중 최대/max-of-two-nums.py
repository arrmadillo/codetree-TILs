import sys

input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    return max(a, b)

print(solution())