#14413 격자판 칠하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]

    # 시작 지점은 0,0

    for r in range(N):
        if arr[0][0] == '#':
            for i in range(0,M,2):
                if arr[r][i] == '?':
                    arr[r][i] = '#'

            for j in range(1,M,2):
                if arr[r][j] == '?':
                    arr[r][j] = '.'

        else:
            for i in range(0, M, 2):
                if arr[r][i] == '?':
                    arr[r][i] = '.'

            for j in range(1, M, 2):
                if arr[r][j] == '?':
                    arr[r][j] = '#'


    for row in arr:
        print(*row)
    print()