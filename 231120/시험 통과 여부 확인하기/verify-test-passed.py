import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    if n >= 80:
        print('pass')
        return
    print(f'{80-n} more score')

solution()