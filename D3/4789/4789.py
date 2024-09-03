#4789 성공적인 공연 기획
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = list(map(int,input()))
    cont = 0
    man = 0

    for i in range(len(arr)):
        cont += arr[i]
        if cont <= i:
            man += 1
            cont += 1

    print(f'#{tc} {man}')