#11804 탐욕_컨테이너 운반
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())  # N = 칸테이너 수  ,    M = 트럭 수
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))

    container.sort(reverse=True)   # 내림차순
    truck.sort(reverse=True)    # 내림차순

    sum_val = 0
    start = 0   # 시작 인덱스 값

    for i in range(N):
        for j in range(start,M):
            if container[i] <= truck[j]:
                sum_val += container[i]
                start += 1
                break

    print(f'#{tc} {sum_val}')