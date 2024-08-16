# 배열순회_대각
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    x,y,N = map(int,input().split())
    arr = [[0]*10 for _ in range(10)]

    # dr = [1]
    # dc = [1]
    #
    # dr2 = [1]
    # dc2 = [-1]
    #
    # for r in range(10):
    #     for c in range(10):
    #         for k in range(1):
    #             for i in range(0,N):
    #                 nr = x + dr[k] * i
    #                 nc = y + dc[k] * i
    #                 if 0 <= nr < 10 and 0<= nc < 10:
    #                     arr[nr][nc] = 1
    #
    # for r in range(10):
    #     for c in range(10):
    #         for k in range(1):
    #             for i in range(0,N):
    #                 nr = x + dr2[k] * i
    #                 nc = y + dc2[k] * i + N - 1
    #                 if 0 <= nr < 10 and 0<= nc < 10:
    #                     arr[nr][nc] = 1
    y2 = y + N-1
    for i in range(N):
        arr[x+i][y+i] =1
        arr[x+i][y2-i] = 1

    print(f'#{tc}')
    for row in arr:
        print(*row)