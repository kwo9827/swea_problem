import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    possible = True
    for r in range(N):
        for c in range(M):
            if arr[r][c] == '#':
                start = '#'
                end = '.'
                break
            elif arr[r][c] == '.':
                start = '.'
                end = '#'
                break
        if arr[r][c] != '?':
            break

    for r in range(N):
        for c in range(M):
            if (r + c) % 2 == 0:
                if arr[r][c] != '?' and arr[r][c] != start:
                    possible = False
                    break
            else:
                if arr[r][c] != '?' and arr[r][c] != end:
                    possible = False
                    break
        if not possible:
            break

    if possible:
        print(f'#{tc} possible')
    else:
        print(f'#{tc} impossible')


