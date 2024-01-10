import sys

input = sys.stdin.readline

def solution():
    score = int(input())
    return 'pass' if score == 100 else 'failure'

print(solution())