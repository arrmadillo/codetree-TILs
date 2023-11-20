import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    if n < 5:
        print(n**2, 'tiny', sep='\n')
        return
    print(n**2)

solution()