# 11315 오목 판정
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]  # 바둑판
    result = 'NO'

    dr = [0,-1,-1,-1]
    dc = [1,1,0,-1]

    for r in range(N):
        for c in range(N):
            for k in range(4):   # 우, 우하, 하, 좌하 확인
                cont = 0  # 연속한 돌의 수
                for i in range(5):  # 본인포함 5개까지 확인
                    nr = r + dr[k] * i
                    nc = c + dc[k] * i
                    if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 'o':
                        cont += 1
                        if cont >= 5:
                            result = 'YES'
                            break

    print(f'#{tc} {result}')

