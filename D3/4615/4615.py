# 4615 오셀로 게임
import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# for tc in range(1,T+1):
#     N,M = map(int,input().split())    # N 가로세로 ,  M 돌 놓는 횟수
#     arr = [[0] * N for _ in range(N)]  # 보드 게임판
#
#     dr = [-1,-1,-1,0,1,1,1,0]
#     dc = [-1,0,1,1,1,0,-1,-1]
#
#     black = 0
#     white = 0
#
#     mid = N//2
#
#     arr[mid][mid] = 2      # 백돌 = 2, 흑돌 = 1  백돌과 흑돌의 초기위치
#     arr[mid-1][mid-1] = 2
#     arr[mid-1][mid] = 1
#     arr[mid][mid-1] = 1
#
#     for _ in range(M):
#         r,c,dol = map(int,input().split())
#         # 입력 좌표는 1~N 사이의 값
#         r -= 1
#         c -= 1
#
#         arr[r][c] = dol
#
#         for i in range(8):  # 8방향 확인
#             pos = []  # 좌표값을 저장하기
#             for j in range(1,N):
#                 nr = r + dr[i] * j
#                 nc = c + dc[i] * j
#                 if nr < 0 or nr >= N or nc < 0 or nc >= N:
#                     break
#                 #arr[nr][nr] -> 0,1,2에 대해 처리
#                 if arr[nr][nc] == 0:
#                     break
#                 if arr[nr][nc] == dol: # 같은 색의 돌을 만나면
#                     for a,b in pos:
#                         arr[a][b] = dol
#                     break
#                 else:  # 다른색의 돌의 위치를 저장하면서 간다.
#                     pos.append([nr,nc])
#
#     for n in range(N):
#         for m in range(N):
#             if arr[n][m] == 1:
#                 black +=1
#             if arr[n][m] == 2:
#                 white +=1
#
#     print(f'#{tc} {black} {white}')

# --------------------------------
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())    # N 가로세로 ,  M 돌 놓는 횟수
    arr = [[0] * N for _ in range(N)]  # 보드 게임판

    dr = [-1,-1,-1,0,1,1,1,0]
    dc = [-1,0,1,1,1,0,-1,-1]

    black = 0
    white = 0

    mid = N//2

    arr[mid][mid] = 2      # 백돌 = 2, 흑돌 = 1  백돌과 흑돌의 초기위치
    arr[mid-1][mid-1] = 2
    arr[mid-1][mid] = 1
    arr[mid][mid-1] = 1

    for _ in range(M):
        r,c,dol = map(int,input().split())
        # 입력 좌표는 1~N 사이의 값
        r -= 1
        c -= 1

        arr[r][c] = dol

        for i in range(8):  # 8방향 확인
            nr,nc = r + dr[i], c + dc[i]
            while 0<= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0:
                    break
                if arr[nr][nc] == dol:
                    nr,nc = nr - dr[i], nc - dc[i]
                    while r != nr or c != nc:
                        arr[nr][nc] = dol
                        nr,nc = nr-dr[i],nc-dc[i]
                    break

                nr,nc = nr+dr[i], nc + dc[i]

    for n in range(N):
        for m in range(N):
            if arr[n][m] == 1:
                black +=1
            if arr[n][m] == 2:
                white +=1

    print(f'#{tc} {black} {white}')
