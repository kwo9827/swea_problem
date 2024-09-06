import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    result = n * m

    for x in range(1, n - 1):
        for y in range(x + 1, n):
            w = b = r = 0
            for r1 in range(x):
                for c1 in range(m):
                    if arr[r1][c1] != 'W':
                        w += 1

            for r2 in range(x, y):
                for c2 in range(m):
                    if arr[r2][c2] != 'B':
                        b += 1

            for r3 in range(y, n):
                for c3 in range(m):
                    if arr[r3][c3] != 'R':
                        r += 1

            tmp = w + b + r

            if result > tmp:
                result = tmp

    print(f'#{tc} {result}')
