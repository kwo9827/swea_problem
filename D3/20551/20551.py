#20551 증가하는 사탕 수열
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    A,B,C = map(int,input().split())

    cont = 0

    while True:
        if A >= B:
            A -= 1
            cont+=1
            if A == 0 or B == 0 or C == 0:
                print(f'#{tc} {-1}')
                break

        if B >= C:
            B -= 1
            cont+=1
            if A == 0 or B == 0 or C == 0:
                print(f'#{tc} {-1}')
                break

        if A<B and B<C:
            print(f'#{tc} {cont}')
            break

