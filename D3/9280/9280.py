#9280 진용이네 주차타워
import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    R_lst = []     # 단위 무게당 요금 (주차장)
    for _ in range(N):
        R = int(input())
        R_lst.append(R)

    W_lst = []     # 차량의 무게
    for _ in range(M):
        W = int(input())
        W_lst.append(W)

    sum_val = 0   # 주차요금

    lst = [0] * len(R_lst)   # 주차장 길이만큼 배열 하나 만들기
    visit = deque()   # 주차장이 꽉차면 대기 장소

    for _ in range(2*M):
        x = int(input())   # x가 음수면 주차장 나감, 양수면 주차장 들어옴
        if x > 0:      # 양수가 들어오면
            for i in range(len(lst)):   # 주차장을 돌면서 0이 있으면 거기 넣기
                if lst[i] == 0:    # 비어있으면 넣기
                    lst[i] = x
                    break
            else:     # (for - else) 만약 주차장이 꽉 차있으면
                visit.append(x)    # 대기 장소에 넣어놓기

        else:       # 양수가 아니라 음수가 들어올때
            A = lst.index(abs(x))    # x의 절댓값에 해당하는 인덱스 위치 찾기
            sum_val += W_lst[abs(x)-1] * R_lst[A]   # 주차 요금에 더하기
            lst[A] = 0    # 0으로 초기화
            if visit:      # 차를 빼고 대기 장소에 차가 기다리고 있으면
                B = visit.popleft()    # 들어온 순서대로 빼주고
                lst[A] = B         # 주차공간에 채워넣기

    print(f'#{tc} {sum_val}')