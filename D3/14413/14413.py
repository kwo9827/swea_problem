#14413 격자판 칠하기
import sys
sys.stdin = open('input.txt')

T = int(input())

def is_possible(N, M, arr):
    # 초기 상태에 따라 격자를 칠할 수 있는지 확인하는 함수
    for start_color in ['#', '.']:
        valid = True
        board = [[0] * M for _ in range(N)]

        # 초기 색칠 시작
        for r in range(N):
            for c in range(M):
                if (r + c) % 2 == 0:
                    expected_color = start_color
                else:
                    expected_color = '#' if start_color == '.' else '.'

                if arr[r][c] == '?':
                    board[r][c] = expected_color
                elif arr[r][c] != expected_color:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            return True
    return False

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    if is_possible(N, M, arr):
        print(f'#{tc} possible')
    else:
        print(f'#{tc} impossible')
