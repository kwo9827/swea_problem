# 9367 당근의 개수
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 당근의 길이
    C = list(map(int,input().split()))

    cont = 1
    max_cont = 0

    for i in range(1,N):
        if C[i] > C[i-1]:
            cont += 1

        else:
            cont = 1

        if cont > max_cont:
            max_cont = cont

    print(f'#{tc} {max_cont}')