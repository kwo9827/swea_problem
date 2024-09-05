#13732 정사각형 확인
import sys
sys.stdin = open('input.txt')

def check_rect(arr, r1, c1, r2, c2):
    # 행과 열의 길이 같은지
    if r2 - r1 != c2 - c1:
        return False
    # 사각영역이 모두 #으로 채워져 있는지
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if arr[r][c] != '#':
                return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    r1 = c1 = N  # 좌상단 좌표> #의 좌표중에 최소 행, 열값
    r2 = c2 = 0  # 우하단 좌표> #의 좌표중에 최대 행, 열값
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '.':
                continue
            # '#'이면 비교
            r1 = min(r1, r)
            c1 = min(c1, c)
            r2 = max(r2, r)
            c2 = max(c2, c)

    ans = 'no'
    if check_rect(arr, r1, c1, r2, c2):
        ans = 'yes'
    print(f'#{tc} {ans}')