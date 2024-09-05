#1865 동철이의 일 분배
import sys
sys.stdin = open('input.txt')

def kfc(visit_num, lotto):
    global max_lotto

    if lotto <= max_lotto:
        return

    if visit_num == N:
        if lotto > max_lotto:
            max_lotto = lotto
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            kfc(visit_num + 1, lotto * (arr[visit_num][i] * 0.01))
            visited[i] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    max_lotto = 0.0
    kfc(0, 1)

    print(f'#{tc} {max_lotto * 100:.6f}')
