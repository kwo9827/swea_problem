import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    min_cont = float('inf')

    for x in range(1, N-1):
        for y in range(x+1, N):
            white = 0
            blue = 0
            red = 0

            for r in range(0, x):
                for c in range(M):
                    if arr[r][c] != 'W':
                        white += 1

            for r in range(x, y):
                for c in range(M):
                    if arr[r][c] != 'B':
                        blue += 1

            for r in range(y, N):
                for c in range(M):
                    if arr[r][c] != 'R':
                        red += 1

            sum_val = white + blue + red

            if sum_val < min_cont:
                min_cont = sum_val

    print(f'#{tc} {min_cont}')
