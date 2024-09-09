import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_cont = 0

    for r in range(N):
        cont = 0
        for c in range(M):
            if arr[r][c] == 1:
                cont += 1

            if arr[r][c] == 0 or c == M-1:
                if cont > max_cont:
                    max_cont = cont
                cont = 0

    for c in range(M):
        cont = 0
        for r in range(N):
            if arr[r][c] == 1:
                cont += 1

            if arr[r][c] == 0 or r == N - 1:
                if cont > max_cont:
                    max_cont = cont
                cont = 0

    if max_cont == 1:
        max_cont = 0

    print(f'#{tc} {max_cont}')