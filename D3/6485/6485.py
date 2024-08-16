import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    busway = [0] * 5001

    for _ in range(N):
        A,B = map(int,input().split())   # A,B 버스 노선
        for i in range(A,B+1):
            busway[i] += 1  # 노선에 1더해서 몇번 지나가는지 확인

    P = int(input())    # 출력해야 할 버스정류장 번호
    busway_number = []  # 버스정류장 번호 저장

    for _ in range(P):
        C = int(input())
        busway_number.append(busway[C])   # 버스정류장 번호 인덱스로 노선의 숫자 확인

    print(f'#{tc}',*busway_number)


