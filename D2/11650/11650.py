# 11650 큐_피자굽기_확인용
import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())     # N: 피자가 들어갈 수 있는 오븐 용량,  M: 피자개수
    pizza = list(map(int,input().split()))
    oven = deque()   # Q

    for i in range(N):   # N개만큼 저장
        oven.append([pizza[i],i+1])   #피자의 인덱스를 어떻게 처리할까 하다가 오븐에 피자와 피자 고유 인덱스 번호를 같이 저장
    # oven =[[치즈양, 피자 넘버]
    start = N     # 남은 피자의 인덱스 시작 번호
    while len(oven) != 1:
        A = oven.popleft()   # 피자를 꺼내라.  A[치즈양][피자번호]
        cheese = A[0]   # ex) 100
        pizza_number = A[1]  # 피자 고유 인덱스

        cheese = cheese//2    # 치즈양이 반으로 줄어듬  -> 50

        if cheese != 0:     # 치즈의 양이 0이 아니면
            oven.append([cheese,pizza_number])  # 치즈는 줄어들지만?? 피자의 인덱스 번호는 그대로이다.

        else:   # 치즈의 양이 0이면
            if start < M:    # 피자의 마지막 인덱스보다 남은 피자 인덱스가 적으면
                oven.append([pizza[start],start+1])   # 다음 피자를 추가
                start += 1

    ans = oven[0][1]   # 오븐에 마지막으로 남아있는 피자의 인덱스 번호를 출력
    print(f'#{tc} {ans}')