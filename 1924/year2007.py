# BACKJOON Online Judge #1924
import sys

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# f = sys.stdin
f = open('Week8/1924/data.txt', 'r')

M, D = map(int, f.readline().split())

day = D

for m in range(1,13):
    if m == M:
        break
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        day += 31
    elif m in [4, 6, 9 ,11]:
        day += 30
    else:
        day += 28

print(week[day%7])