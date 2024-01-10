import sys

input = sys.stdin.readline


def solution():
    a = int(input())
    if a >= 90:
        return 'A'
    elif a >= 80:
        return 'B'
    elif a >= 70:
        return 'C'
    elif a >= 60:
        return 'D'
    return 'F'

print(solution())