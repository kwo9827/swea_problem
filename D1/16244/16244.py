# 16244 배열순회_테두리
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    x,y,N = map(int,input().split())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(x,x+N):
        for j in range(y,y+N):
            arr[i][j] = 1

    x2 = x+1
    y2 = y+1

    for i in range(x2, x2 + N -2):
        for j in range(y2, y2 + N-2):
            arr[i][j] = 0

    print(f'#{tc}')
    for row in arr:
        print(*row)
