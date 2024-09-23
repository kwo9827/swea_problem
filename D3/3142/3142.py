#3142 영준이와 신비한 뿔의 숲
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    B = N - M
    A = M - B

    print(f'#{tc} {A} {B}')
