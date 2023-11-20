import sys
input = sys.stdin.readline

num = int(input())

def solution(num):
    if num > 0:
        print(num)
    elif num < 0:
        print(num, "minus", sep='\n')

solution(num)