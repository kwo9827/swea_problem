#12385 배열1_전기버스_확인용
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    K,N,M = map(int,input().split())
    # K = 한번에 갈 수 있는 거리, N = 종점 번호 , M = 충전기 개수
    busway = list(map(int,input().split()))
    lst = [0] * (N+1)    # 노선
    current_pos = 0   # 현재 위치
    result = 0

    for i in busway:  # 충전기가 있는 곳을 노선에 표시
        lst[i] = 1

    for i in range(len(lst)):
        if current_pos + K >= N:
            break

        next_pos = current_pos
        for j in range(current_pos+1, current_pos+1+K):
            if j <= N and lst[j] == 1:
                next_pos = j

        if current_pos == next_pos:
            result = 0
            break

        current_pos = next_pos
        result += 1

    print(f'#{tc} {result}')