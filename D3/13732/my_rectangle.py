import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(str,input())) for _ in range(N)]

    result = 'yes'

    r1 = N
    c1 = N
    r2 = 0
    c2 = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                continue
            r1 = min(r1,r)
            c1 = min(c1,c)
            r2 = max(r2,r)
            c2 = max(c2,c)

    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            if arr[r][c] != '#':
                result = "no"

    if (r2-r1) != (c2-c1):
        result = "no"

    print(f'#{tc} {result}')