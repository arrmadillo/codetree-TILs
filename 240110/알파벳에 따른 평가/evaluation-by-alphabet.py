import sys

input = sys.stdin.readline.rstrip

person = {'S':'Superior', 'A':'Excellent', 'B':'Good', 'C':'Usually', 'D':'Effort'}

def solution():
    a = input()
    return person[a] if a in person.keys() else 'Failure'

print(solution())