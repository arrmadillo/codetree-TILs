import sys

input = sys.stdin.readline

person = {1:'John', 2:'Tom', 3:'Paul'}

def solution():
    a = int(input())
    return 'Vacancy' if a > 3 else person[a]

print(solution())