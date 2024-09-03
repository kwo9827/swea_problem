#14413 격자판 칠하기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = 'possible'

    if arr[0][0] == '.':
        start = '.'
        end = '#'
    elif arr[0][0] == '#':
        start = '#'
        end = '.'
    else:
        # 첫 칸이 '?'인 경우는 초기화 방법이 둘 다 가능하므로 기본값 설정
        start = '#'
        end = '.'

    for r in range(N):
        for c in range(M):
            if arr[r][c] == '?':
                if (r + c) % 2 == 0:
                    arr[r][c] = start
                else:
                    arr[r][c] = end
            else:
                if (r + c) % 2 == 0:
                    check_arr = start
                else:
                    check_arr = end

                if arr[r][c] != check_arr:
                    result = 'impossible'
                    break
        if result == 'impossible':
            break

    print(f'#{tc} {result}')
