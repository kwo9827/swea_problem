import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    min_cont = float('inf')

    for x in range(1,N-1):
        for y in range(x+1,N):
            cont = 0

            for r in range(x):
                for c in range(M):
                    if arr[r][c] != 'W':
                        cont += 1

            for r in range(x,y):
                for c in range(M):
                    if arr[r][c] != 'B':
                        cont += 1

            for r in range(y,N):
                for c in range(M):
                    if arr[r][c] != 'R':
                        cont += 1

            if cont < min_cont:
                min_cont = cont

    print(f'#{tc} {min_cont}')

