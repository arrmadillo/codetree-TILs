import sys

input = sys.stdin.readline

def solution():
    a = int(input())
    if a >= 1:
        return 'High'
    elif a >= 0.5:
        return 'Middle'
    return 'Low'

print(solution())