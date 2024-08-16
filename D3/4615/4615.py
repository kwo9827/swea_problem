# 4615 재미있는 오셀로 게임
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())   # N : 가로세로길이, M = 돌 놓는 횟수

    arr = [[0] * N for _ in range(N)]  # 오셀로 판 만들기
    mid = N // 2  # 중심은 N//2
    arr[mid][mid] = arr[mid - 1][mid - 1] = 1  # 흑돌 초기값
    arr[mid - 1][mid] = arr[mid][mid - 1] = 2  # 백돌 초기값

    dr = [-1,-1,-1,0,1,1,1,0]
    dc = [1,0,-1,-1,-1,0,1,1]

    for _ in range(M):
        y,x,turn = map(int,input().split())  # x좌표, y좌표, 차례
        x -= 1   # 흑돌
        y -= 1   # 백돌
        arr[x][y] = turn

        for r in range(N):
            for c in range(N):
                for k in range(8):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    tmp = []
                    if 0<= nr < N and 0<= nc < N and arr[nr][nc] == 3-turn:
                        tmp.append([nr,nc])
                        nr = nr + r
                        nc = nr + c
                    if 0<= nr < N and 0<= nc < N and arr[nr][nc] == turn:
                        for p,q in tmp:
                            arr[p][q] = turn

    black = 0
    white = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:   # 흑돌 계산
                black += 1
            else:                # 백돌 계산
                white += 1

    for row in arr:
        print(*row)

    print(f'#{tc} {black} {white}')