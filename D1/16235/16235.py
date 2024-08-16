# 16235 배열순회_행우선
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = [[0] * 10 for _ in range(10)]
    x,y,N = map(int,input().split())   # x,y 좌표, N: 사각형 가로세로

    start = 1
    for i in range(x, x + N):
        for j in range(y, y + N):
            arr[i][j] = start
            start += 1

    print(f'#{tc}')
    for row in arr:
        print(*row)