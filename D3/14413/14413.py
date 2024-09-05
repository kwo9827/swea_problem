#14413 격자판 칠하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(N)]
    board = [[] * N for _ in range(M)]

    for r in range(N):
        for c in range(M):
            board[r][c] = arr[r][c]

    for row in board:
        print(*row)

    dr = [0,1,0,-1]
    dc = [-1,0,1,0]

    for r in range(N):
        for c in range(M):
            if arr[r][c] == '?':
                continue
            elif arr[r][c] == '#':
                if (r+c) % 2 == 0:
                    start = '#'
                    end = '.'
                    break

                else:
                    start = '.'
                    end = '#'
                    break
            break
        break



    for r in range(N):
        for c in range(M):
            if (r+c) % 2 == 0:
                if arr[r][c] == '?' and arr[r][c] == start:
                    arr[r][c] = start

                elif arr[r][c] == '?' and arr[r][c] == end:
                    arr[r][c] = end

    for row in arr:
        print(*row)

    print()