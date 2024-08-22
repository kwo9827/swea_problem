#11573 스택_제로
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    stack = [0] * N
    top = -1

    for i in range(N):
        if arr[i] != 0:
            top += 1
            stack[top] = arr[i]

        if arr[i] == 0:
            stack[top] = 0
            top -= 1

    print(f'#{tc} {sum(stack)}')
