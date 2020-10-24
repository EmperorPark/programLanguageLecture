# BACKJOON Online Judge #2839
"""
import sys

def func():
    for i in range(0, 5001, 3):
        # if i % 3 != 0:
        #    continue
        if i > N:
            return -1
        for j in range(0,5001, 5):
            # if j % 5 != 0:
            #    continue
            if i + j == N:
                x = j
                y = i
                return [x, y]
            if i > N and j > N:
                return -1




#f = sys.stdin
f = open('Week8/2839/data.txt', 'r')
N = int(f.readline())

r = func()

if r == -1:
    print(r)
else:
    print(r[0]//5 + r[1]//3)


"""
import sys
f = sys.stdin
#f = open('data.txt', 'r')

N = int(f.readline().rstrip())
temp = N
result = -1

for i in range(0, N, 3):
    temp = N - i
    if temp % 5 == 0:
        result = (temp//5 + i//3)
        break

    if result == -1:
        if N % 3 == 0:
            result = N // 3

print (result)