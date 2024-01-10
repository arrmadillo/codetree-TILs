import sys

input = sys.stdin.readline

def solution():
    temp = int(input())
    if temp < 0:
        return 'ice'
    elif temp >= 100:
        return 'vapor'
    return 'water'

print(solution())