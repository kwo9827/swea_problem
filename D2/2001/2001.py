# 2001 파리퇴치
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_bug = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_bug = 0
            for r in range(i,i+M):
                for c in range(j,j+M):
                    sum_bug += arr[r][c]

            if sum_bug > max_bug:
                max_bug = sum_bug

    print(f'#{tc} {max_bug}')