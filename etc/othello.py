# ```
#
# 1
# 4 12
# 1 2 1
# 1 1 2
# 4 3 1
# 4 4 2
# 2 1 1
# 4 2 2
# 3 4 1
# 1 3 2
# 2 4 1
# 1 4 2
# 4 1 2
# 3 1 2
#
# ```

def f(i,j,bw,N):
    board[i][j] = bw    # 지정된 돌 놓기
    for di,dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        ni,nj = i+di, j+dj
        tmp = []
        while 0<=ni<N and 0<=nj<N and board[ni][nj] == op[bw]:  # 반대색 돌이면
            tmp.append((ni,nj))  # 뒤집을 돌을 저장하고
            ni,nj = ni + di, nj + dj  # 현재 방향으로 계속 이동
        if 0<= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw

B = 1  # 흑돌
W = 2  # 백돌

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N 가로세로 ,  M: 돌 놓는 횟수
    play = [list(map(int,input().split())) for _ in range(M)]  # 돌, 횟수 입력받기

    board = [[0] * N for _ in range(N)] # 보드판준비

    board[N//2-1][N//2-1] = W   # 백돌 시작위치
    board[N//2][N//2] = W

    board[N//2-1][N//2] = B   # 흑돌 시작위치
    board[N//2][N//2-1] = B

    for col,row,bw in play: # 입력순서 주의
        f(row-1,col-1,bw,N)  # 돌 놓기 , 뒤집기

    bcnt = wcnt = 0   # 검은돌 개수, 흰돌 개수
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            else:
                wcnt += 1

    print(f'#{tc} {bcnt} {wcnt}')
