#12387 배열1_구간합_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 정수의 개수,  M = 구간의 개수
    arr = list(map(int,input().split()))

    max_sum = float('-inf')
    min_sum = float('inf')

    for i in range(N-M+1):
        sum = 0
        for j in range(i,i+M):
            sum += arr[j]

        if sum > max_sum:
            max_sum = sum

        if sum < min_sum:
            min_sum = sum

    print(f'#{tc} {max_sum-min_sum}')
