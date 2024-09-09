#22375 스위치 조작
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = list(map(int,input().split()))

    cont = 0

    while arr != result:
        for i in range(len(arr)):
            if arr[i] != result[i]:
                cont += 1
                for j in range(i,len(arr)):
                    arr[j] = 1 - arr[j]


    print(f'#{tc} {cont}')
