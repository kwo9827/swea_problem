#13732 정사각형 판정
import sys
sys.stdin = open('input.txt')


def find_square():
    min_r, min_c = N, N
    max_r, max_c = -1, -1
    count = 0

    # 1. 모든 '#'의 위치를 찾고, 그 범위를 기록합니다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                count += 1
                min_r = min(min_r, i)
                max_r = max(max_r, i)
                min_c = min(min_c, j)
                max_c = max(max_c, j)

    # 2. 찾은 범위가 정사각형인지 확인합니다.
    if (max_r - min_r) == (max_c - min_c):
        expected_size = (max_r - min_r + 1) ** 2
        if expected_size == count:
            return 'yes'

    return 'no'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    result = find_square()
    print(f'#{tc} {result}')