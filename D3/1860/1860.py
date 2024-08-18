# 1860 붕어빵 만들기
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M, K = map(int,input().split())  # N = 리스트길이, M = 붕어빵 만드는데 걸리는 시간, K = 붕어빵 수
    when = list(map(int,input().split()))  # 사람 언제 오는지 리스트
    result = 'Possible'
    when.sort()

    for i in range(N):
        # 리스트의 요소가 걸리는 시간보다 작으면
        # and when[i] -> 해당 손님이 오기전까지 만들수 있는 붕어빵 수가 손님 수보다 작으면
        if when[i] < M or ((when[i]//M)*K) < i+1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')
