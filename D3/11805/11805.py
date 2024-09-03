#11805 탐욕_화물 도크
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s,e = map(int,input().split())
        lst.append((s,e))   # 리스트에 시작 시간, 종료 시간 저장

    lst.sort(key=lambda x: x[1])   # 종료시간을 기준으로 정렬
    # print(lst)
    cont = 0
    new_e = 0

    for s,e in lst:    # 리스트에서 시작 시간, 종료 시간 가져옴
        if s >= new_e:  # 다음 시작 시간이 종료시간보다 같거나 크면
            cont += 1   # 카운트 증가시키고
            new_e = e   # 종료시간 갱신해줌

    print(f'#{tc} {cont}')
