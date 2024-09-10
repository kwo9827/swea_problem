#13038 교환학생
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    cont = 0
    value = 0
    i = 0

    while N != 0:
        if arr[i] == 1:
            N -= 1
            cont += 1
            i += 1

        else:
            i += 1
            if cont >= 1:
                cont += 1

        if i == len(arr):
            i = 0

    print(f'#{tc} {cont}')
