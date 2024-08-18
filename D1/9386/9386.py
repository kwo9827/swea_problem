# 9386 연속한 1의 개수
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())  # 배열 길이
    arr = list(input())

    cont = 0
    max_cont = 0

    for i in range(N):
        if arr[i] == '1':
            cont += 1
        else:
            cont = 0

        if cont > max_cont:
            max_cont = cont

    print(f'#{tc} {max_cont}')