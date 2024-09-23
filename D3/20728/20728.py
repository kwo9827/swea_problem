#20728 공평한 분배2
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()
    min_val = 99999999999

    for i in range(N-K+1):
        value = arr[i+K-1] - arr[i]
        min_val = min(min_val, value)

    print(f'#{tc} {min_val}')
