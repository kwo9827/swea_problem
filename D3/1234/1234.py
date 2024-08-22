#1234 10일차_비밀번호
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N, pwd = input().split()
    N = int(N)

    top = -1
    stack = [0] * N

    for i in range(N):
        if pwd[i] == stack[top]:
            stack[top] = 0
            top -= 1

        else:
            top += 1
            stack[top] = pwd[i]

    lst = []

    for j in stack:
        if j != 0:
            lst.append(j)

    result = ''.join(lst)

    print(f'#{tc} {result}')