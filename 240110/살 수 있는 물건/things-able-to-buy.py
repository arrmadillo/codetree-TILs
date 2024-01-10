import sys

input = sys.stdin.readline

def solution():
    money = int(input())
    if money >= 3000:
        return 'book'
    elif money >= 1000:
        return 'mask'
    return 'no'

print(solution())