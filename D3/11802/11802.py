#11802 완전검색_최소합
import sys
sys.stdin = open('input.txt')

def kfc(r,c,sum_val):
    global min_sum
    if r == N-1 and c == N-1:
        if sum_val < min_sum:
            min_sum = sum_val

    if sum_val > min_sum:
        return

    if c+1 < N:
        kfc(r,c+1,sum_val+arr[r][c+1])
    if r+1 < N:
        kfc(r+1,c,sum_val+arr[r+1][c])

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_sum = 999999999

    kfc(0,0,arr[0][0])    # r, c , sum
    print(f'#{tc} {min_sum}')