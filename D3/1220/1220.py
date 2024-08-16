# 1220 Magnetic
import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]  # N극 = 1 , S극 = 2

    cont = 0 # 교착상태의 수

    for i in range(N):   # N극이 S극보다 위에 위치함
        check = 0        # 교착상태를 의미함
        for j in range(N):
            if arr[j][i] == 1:
                check = 1

            elif arr[j][i] == 2:
                if check == 1:  # N극을 만나고 밑으로 내려가다가 S극을 만나면
                    cont += 1   # cont 증가
                    check = 0
                check = 0

    print(f'#{tc} {cont}')