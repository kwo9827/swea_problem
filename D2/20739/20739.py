#20739 고대 유적2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]  # 유적

    max_len = 0

    for r in range(N):  # 가로 검사
        cont = 0
        for c in range(M):
            if arr[r][c] == 1:
                cont += 1
                if cont > max_len:
                    max_len = cont
            else:
                cont = 0

    for c in range(M):  # 세로 검사
        cont = 0
        for r in range(N):
            if arr[r][c] == 1:
                cont += 1
                if cont > max_len:
                    max_len = cont
            else:
                cont = 0

    if max_len == 1:
        max_len = 0

    print(f'#{tc} {max_len}')