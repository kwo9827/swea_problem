#11012 배열2_사각영역들의 합
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 가로세로 ,  M = 목표 사각형
    arr = [list(map(int,input().split())) for _ in range(N)]
    sum = 0
    for _ in range(M):
        r1,c1,line = map(int,input().split())
        for r in range(r1,min(r1+line,N)):
            for c in range(c1,min(c1+line,N)):
                sum += arr[r][c]
                arr[r][c] = 0

    print(f'#{tc} {sum}')

