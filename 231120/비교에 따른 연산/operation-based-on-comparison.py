import sys

input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    if a == max(a, b):
        print(a*b)
        return
    print(b//a)

solution()