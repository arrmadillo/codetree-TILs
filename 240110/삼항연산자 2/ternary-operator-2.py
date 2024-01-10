import sys

input = sys.stdin.readline

def solution():
    a = int(input())
    return 't' if a == 1 else 'f'

print(solution())