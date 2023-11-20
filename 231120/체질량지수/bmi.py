import sys

input = sys.stdin.readline


def solution():
    cm, kg = map(int, input().split())
    m = 0.01 * cm
    bmi = kg // (m**2)
    if bmi >= 25:
        print(f'{bmi:.0f}', 'Obesity', sep='\n')
    else:
        print(f'{bmi:.0f}')

solution()