import sys

input = sys.stdin.readline

def solution():
    a = float(input())
    if a >= 1.0:
        return 'High'
    elif a >= 0.5:
        return 'Middle'
    return 'Low'

print(solution())